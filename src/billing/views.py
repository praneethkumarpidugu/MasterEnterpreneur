from django.shortcuts import render
from .models import Transaction
# Create your views here.
import random

def upgrade(request):
    Transaction.objects.create_new(request.user, "asdafjafhjahf%s"%(random.randint(0,100)), 25.00, "visa")
    return render(request, "billing/upgrade.html", {})

def billing_history(request):
    history = Transaction.objects.filter(user=request.user).filter(success=True)
    return render(request, "billing/history.html", {"queryset": history})