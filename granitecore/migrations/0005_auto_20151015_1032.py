# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('granitecore', '0004_auto_20151014_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlainTextAsset',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
                ('text', models.TextField(default='')),
            ],
        ),
        migrations.RenameModel(
            old_name='Asset',
            new_name='FileAsset',
        ),
        migrations.RemoveField(
            model_name='page',
            name='site',
        ),
        migrations.RemoveField(
            model_name='template',
            name='site',
        ),
        migrations.RemoveField(
            model_name='website',
            name='brand_large',
        ),
        migrations.RemoveField(
            model_name='website',
            name='brand_medium',
        ),
        migrations.RemoveField(
            model_name='website',
            name='brand_original',
        ),
        migrations.RemoveField(
            model_name='website',
            name='brand_small',
        ),
        migrations.RemoveField(
            model_name='website',
            name='favicon',
        ),
        migrations.AddField(
            model_name='page',
            name='role',
            field=models.CharField(choices=[('NN', 'Standard Page'), ('HM', 'Home Page'), ('ER', 'Error Page')], max_length=2, default='NN'),
        ),
        migrations.AddField(
            model_name='website',
            name='authors',
            field=models.CharField(max_length=255, default='Matthew McGowan'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='website',
            name='handle',
            field=models.CharField(max_length=100, default='test'),
            preserve_default=False,
        ),
    ]
