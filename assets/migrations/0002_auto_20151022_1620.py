# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import granite.utils.cache


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileasset',
            name='file',
            field=models.FileField(upload_to=granite.utils.cache.path_and_rename),
        ),
    ]
