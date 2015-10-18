# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('granitecore', '0015_auto_20151018_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='site',
        ),
        migrations.RemoveField(
            model_name='fileasset',
            name='asset_ptr',
        ),
        migrations.RemoveField(
            model_name='plaintextasset',
            name='asset_ptr',
        ),
        migrations.AddField(
            model_name='fileasset',
            name='handle',
            field=models.CharField(max_length=48, default='styles.css'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fileasset',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=2, verbose_name='ID', serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fileasset',
            name='site',
            field=models.ForeignKey(to='granitecore.Website', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plaintextasset',
            name='handle',
            field=models.CharField(max_length=48, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plaintextasset',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=3, verbose_name='ID', serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plaintextasset',
            name='site',
            field=models.ForeignKey(to='granitecore.Website', default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Asset',
        ),
    ]
