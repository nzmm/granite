# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('granitecore', '0003_auto_20151014_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='site',
            field=models.ForeignKey(to='granitecore.Website', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='template',
            name='site',
            field=models.ForeignKey(to='granitecore.Website', default=1),
            preserve_default=False,
        ),
    ]
