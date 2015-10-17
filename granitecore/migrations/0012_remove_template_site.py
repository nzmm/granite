# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('granitecore', '0011_auto_20151018_0903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='template',
            name='site',
        ),
    ]
