# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('granitecore', '0010_auto_20151017_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileasset',
            name='site',
            field=models.ForeignKey(to='granitecore.Website', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='site',
            field=models.ForeignKey(to='granitecore.Website', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plaintextasset',
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
