# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('granitecore', '0013_template_site'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='mauthor',
            new_name='page_author',
        ),
    ]
