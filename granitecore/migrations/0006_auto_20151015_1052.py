# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('granitecore', '0005_auto_20151015_1032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='template',
            old_name='text',
            new_name='markup',
        ),
    ]
