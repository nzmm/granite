# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='website',
            old_name='domain',
            new_name='hosts',
        ),
    ]
