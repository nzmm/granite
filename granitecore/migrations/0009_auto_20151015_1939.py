# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('granitecore', '0008_auto_20151015_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='publish_at',
        ),
        migrations.RemoveField(
            model_name='page',
            name='published_at',
        ),
        migrations.RemoveField(
            model_name='page',
            name='unpublish_at',
        ),
    ]
