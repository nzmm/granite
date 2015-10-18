# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('granitecore', '0017_auto_20151018_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='page_description',
            field=models.CharField(default='', max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='website',
            name='description',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fileasset',
            name='file',
            field=models.FileField(upload_to='assets'),
        ),
    ]
