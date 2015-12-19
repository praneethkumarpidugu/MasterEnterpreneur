# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0008_auto_20151216_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='share_message',
            field=models.TextField(default=b'\ncheck out this video\n'),
            preserve_default=True,
        ),
    ]
