# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_end', models.DateTimeField(default=datetime.datetime(2016, 2, 4, 4, 51, 17, 477813, tzinfo=utc), verbose_name=b'End Date')),
                ('date_start', models.DateTimeField(default=datetime.datetime(2016, 2, 4, 4, 51, 17, 477927, tzinfo=utc), verbose_name=b'Start Date')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
