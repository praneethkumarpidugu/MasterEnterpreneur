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
    if request.user.is_authenticated():
        try:
            #something to get the current customer id stored somewhere
            merchant_customer_id = UserMerchantId.objects.get(user=request.user).customer_id
        except UserMerchantId.DoesNotExist:
            new_customer_result = braintree.Customer.create({})
            if new_customer_result.is_success:
                merchant_customer_id = UserMerchantId.objects.create(user=request.user)
                merchant_customer_id.customer_id = new_customer_result.customer.id
                merchant_customer_id.save()
                print """Customer created with id = {0}""".format(new_customer_result.customer.id)
            else:
                print "Error: {0}".format(new_customer_result.message)
                #redirect somewhere
        except:
            #some error
            #redirect somewhere
            pass
        trans = Transaction.objects.create_new(request.user,\
                                               "asdafjafhjahf%s"%(random.randint(0,100)),\
                                               25.00, "visa")
        if trans.success:
            membership_instance, created = Membership.objects.get_or_create(user=request.user)
            membership_dates_update.send(membership_instance, new_date_start = trans.timestamp)
    return render(request, "billing/upgrade.html", {})

