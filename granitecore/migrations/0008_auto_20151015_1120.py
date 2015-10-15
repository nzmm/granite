# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('granitecore', '0007_auto_20151015_1102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fileasset',
            old_name='name',
            new_name='handle',
        ),
        migrations.RenameField(
            model_name='plaintextasset',
            old_name='name',
            new_name='handle',
        ),
    ]
