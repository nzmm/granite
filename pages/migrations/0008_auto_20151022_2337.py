# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20151019_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1001, 'Top-level Page'), (999, 'Sub-level Page'), (1000, 'Home Page'), (400, 'Client Error Page (4xx)'), (500, 'Server Error Page (5xx)')], default=1001),
        ),
    ]
