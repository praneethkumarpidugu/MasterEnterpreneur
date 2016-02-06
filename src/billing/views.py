from django.shortcuts import render
from .models import Membership,Transaction,UserMerchantId
from .signals import membership_dates_update
# Create your views here.
import random

import braintree

braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id="85rcwqpqqj3hbn98",
                                  public_key="j5d5khw4qp3j6jpg",
                                  private_key="a8dde433bb2920067b3dccb5abb82274")

PLAN_ID = "monthly_plan"

def billing_history(request):
    history = Transaction.objects.filter(user=request.user).filter(success=True)
    return render(request, "billing/history.html", {"queryset": history})

def upgrade(request):
    client_token = braintree.ClientToken.generate()
    if request.user.is_authenticated():
        try:
            #something to get the current customer id stored somewhere
            merchant_obj = UserMerchantId.objects.get(user=request.user)
        except UserMerchantId.DoesNotExist:
            new_customer_result = braintree.Customer.create({})
            if new_customer_result.is_success:
                merchant_obj, created = UserMerchantId.objects.get_or_create(user=request.user)
                merchant_obj.customer_id = new_customer_result.customer.id
                merchant_obj.save()
                print """Customer created with id = {0}""".format(new_customer_result.customer.id)
            else:
                print "Error: {0}".format(new_customer_result.message)
                #redirect somewhere
        except:
            #some error
            #redirect somewhere
            pass
        merchant_customer_id = merchant_obj.customer_id
        if request.method == "POST":
            nonce = request.POST.get("payment_method_nonce", None)
            if nonce is not None:
                customer_update_result = braintree.Customer.update(merchant_customer_id, {
                    "payment_method_nonce": nonce
                })
                credit_card_token = customer_update_result.customer.credit_cards[0].token
                # customer_card = braintree.Customer.find(merchant_customer_id).credit_cards[0].token
                subscription_result = braintree.Subscription.create({
                    "payment_method_token": credit_card_token,
                    "plan_id": PLAN_ID
                })
                if subscription_result.is_success:
                    trans_id = subscription_result.subscription.id
                    trans = Transaction.objects.create_new(request.user,trans_id,25.00, "visa")
                    if trans.success:
                        membership_instance, created = Membership.objects.get_or_create(user=request.user)
                        membership_dates_update.send(membership_instance, new_date_start=trans.timestamp)
                else:
                    print "failed"

    context = {"client_token": client_token}
    return render(request, "billing/upgrade.html", context)

