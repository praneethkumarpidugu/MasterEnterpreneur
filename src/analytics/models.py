from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from .signals import page_view

class PageView(models.Model):
    path = models.CharField(max_length=350)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    #count = models.PositiveIntegerField(default=1)
    timestamp = models.DateTimeField(default=timezone.now())

    def __unicode__(self):
        return self.path

def page_view_received(sender, page_path, *args, **kwargs):
    user = sender
    if not user.is_authenticated():
        new_page_view = PageView.objects.create(path=page_path, timestamp=timezone.now())
    else:
        new_page_view = PageView.objects.create(path=page_path, user=user, timestamp=timezone.now())
    # if not created:
    #     new_page_view.count += 1
    #     new_page_view.save()

page_view.connect(page_view_received)