from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Membership,Transaction,UserMerchantId
from .signals import membership_dates_update
# Create your views here.
import random

import braintree

braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id=settings.BRAINTREE_MERCHANT_ID,
                                  public_key=settings.BRAINTREE_PUBLIC_KEY,
                                  private_key=settings.BRAINTREE_PRIVATE_KEY)

PLAN_ID = "monthly_plan"

def billing_history(request):
    history = Transaction.objects.filter(user=request.user).filter(success=True)
    return render(request, "billing/history.html", {"queryset": history})

def upgrade(request):

    if request.user.is_authenticated():
        try:
            merchant_obj = UserMerchantId.objects.get(user=request.user)
        except:
            messages.error(request, "There was an error with your account. Please contact us.")
            return redirect("contact_us")
        merchant_customer_id = merchant_obj.customer_id
        client_token = braintree.ClientToken.generate({
            "customer_id": merchant_customer_id
        })
        if request.method == "POST":
            nonce = request.POST.get("payment_method_nonce", None)
            if nonce is None:
                messages.error(request, "An error occured, please try again")
                return redirect("account_upgrade")
            else:
                payment_method_result = braintree.PaymentMethod.create({
                    "customer_id": merchant_customer_id,
                    "payment_method_nonce": nonce,
                    "options": {
                        "make_default": True
                    }
                    })
                if not payment_method_result.is_success:
                    messages.error(request, "An error occured: %s" %(payment_method_result.message))
                    return redirect("account_upgrade")

                the_token = payment_method_result.payment_method.token
                current_sub_id = merchant_obj.subscription_id
                current_plan_id = merchant_obj.plan_id
                did_create_sub = False
                did_update_sub = False
                trans_success = False
                trans_timestamp = None

                try:
                    current_subscription = braintree.Subscription.find(current_sub_id)
                    sub_status = current_subscription.status
                except:
                    current_subscription = None
                    sub_status = None
                if current_subscription and sub_status == "Active":
                    update_sub = braintree.Subscription.update(current_sub_id,{
                            "payment_method_token": the_token,
                        })
                    did_update_sub = True
                else:
                    create_sub = braintree.Subscription.create({
                             "payment_method_token": the_token,
                             "plan_id": PLAN_ID
                        })
                    did_create_sub = True

                if did_create_sub or did_update_sub:
                    membership_instance, created = Membership.objects.get_or_create(user=request.user)

                if did_update_sub and not did_create_sub:
                    messages.success(request, "Your plan has been updated")
                    membership_dates_update.send(membership_instance, new_date_start=timezone.now())
                    return redirect("billing_history")
                elif did_create_sub and not did_update_sub:
                    merchant_obj.subscription_id = create_sub.subscription.id
                    merchant_obj.plan_id = PLAN_ID
                    merchant_obj.save()
                    payment_type = create_sub.subscription.transactions[0].payment_instrument_type
                    trans_id = create_sub.subscription.transactions[0].id
                    sub_id = create_sub.subscription.id
                    sub_amount = create_sub.subscription.price

                    if payment_type == braintree.PaymentInstrumentType.PayPalAccount:
                        trans = Transaction.objects.create_new(request.user,trans_id,sub_amount, "PayPal")
                        trans_success = trans.success
                        trans_timestamp = trans.timestamp
                    elif payment_type == braintree.PaymentInstrumentType.CreditCard:
                        credit_card_details = create_sub.subscription.transactions[0].credit_card_details
                        card_type = credit_card_details.card_type
                        last_4 = credit_card_details.last_4
                        trans = Transaction.objects.create_new(request.user,trans_id,sub_amount, card_type, last_four=last_4)
                        trans_success = trans.success
                        trans_timestamp = trans.timestamp
                    else:
                        trans_success = False
                    membership_dates_update.send(membership_instance, new_date_start=trans_timestamp)
                    messages.success(request, "Welcome to our service")
                    return redirect("billing_history")
                else:
                    messages.error(request, "An error occured, please try again")
                    return redirect("account_upgrade")

    context = {"client_token": client_token}
    return render(request, "billing/upgrade.html", context)

