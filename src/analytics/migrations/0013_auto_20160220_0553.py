# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0012_auto_20160211_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageview',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 20, 5, 53, 53, 948934, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
