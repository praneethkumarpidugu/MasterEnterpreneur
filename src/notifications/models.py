from django.db import models

# Create your models here.
from .signals import notify

def new_notification(sender, recipient, action, *args, **kwargs):
    print recipient
    print action
    print sender
    print args
    print kwargs

notify.connect(new_notification)