# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import granite.validators


class Migration(migrations.Migration):

    dependencies = [
        ('granitecore', '0014_auto_20151018_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('handle', models.CharField(max_length=48)),
                ('site', models.ForeignKey(to='granitecore.Website')),
            ],
        ),
        migrations.RemoveField(
            model_name='fileasset',
            name='handle',
        ),
        migrations.RemoveField(
            model_name='fileasset',
            name='id',
        ),
        migrations.RemoveField(
            model_name='fileasset',
            name='site',
        ),
        migrations.RemoveField(
            model_name='plaintextasset',
            name='handle',
        ),
        migrations.RemoveField(
            model_name='plaintextasset',
            name='id',
        ),
        migrations.RemoveField(
            model_name='plaintextasset',
            name='site',
        ),
        migrations.AlterField(
            model_name='page',
            name='handle',
            field=models.CharField(max_length=100, validators=[granite.validators.validate_page_handle], default='/pages/'),
        ),
        migrations.AddField(
            model_name='fileasset',
            name='asset_ptr',
            field=models.OneToOneField(parent_link=True, serialize=False, primary_key=True, to='granitecore.Asset', auto_created=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plaintextasset',
            name='asset_ptr',
            field=models.OneToOneField(parent_link=True, serialize=False, primary_key=True, to='granitecore.Asset', auto_created=True, default=1),
            preserve_default=False,
        ),
    ]
