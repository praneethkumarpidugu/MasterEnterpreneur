# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0013_auto_20160109_2230'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title', 'timestamp']},
        ),
        migrations.AddField(
            model_name='video',
            name='order',
            field=models.PositiveIntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to=b'images/', blank=True),
            preserve_default=True,
        ),
    ]
