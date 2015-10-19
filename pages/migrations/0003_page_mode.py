# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20151019_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='mode',
            field=models.CharField(choices=[('MD', 'Markdown'), ('HT', 'HTML')], max_length=2, default='MD'),
        ),
    ]
