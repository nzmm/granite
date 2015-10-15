# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('granitecore', '0006_auto_20151015_1052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='visible',
        ),
        migrations.AddField(
            model_name='page',
            name='published_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 10, 15, 11, 2, 4, 206618, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='page',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
