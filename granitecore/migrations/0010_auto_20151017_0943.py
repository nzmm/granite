# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('granitecore', '0009_auto_20151015_1939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='template',
            old_name='name',
            new_name='handle',
        ),
    ]
