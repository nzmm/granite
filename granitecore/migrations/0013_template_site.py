# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('granitecore', '0012_remove_template_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='site',
            field=models.ForeignKey(default=1, to='granitecore.Website'),
            preserve_default=False,
        ),
    ]
