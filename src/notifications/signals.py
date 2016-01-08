#https://docs.djangoproject.com/en/1.7/topics/signals/#defining-and-sending-signals

from django.dispatch import Signal

notify = Signal(providing_args=['user', 'action'])
