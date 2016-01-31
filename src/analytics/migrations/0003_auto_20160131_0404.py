# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_pageview_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pageview',
            name='count',
        ),
        migrations.AlterField(
            model_name='pageview',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 31, 4, 4, 46, 743968, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
