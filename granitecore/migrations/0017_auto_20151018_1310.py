# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('granitecore', '0016_auto_20151018_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='quick_link',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fileasset',
            name='file',
            field=models.FileField(upload_to='assets/gen/'),
        ),
    ]
