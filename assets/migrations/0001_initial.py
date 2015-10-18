# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import granite.core.objects


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileAsset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('handle', models.CharField(max_length=48)),
                ('file', models.FileField(upload_to='assets/static')),
                ('site', models.ForeignKey(to='websites.Website')),
            ],
        ),
        migrations.CreateModel(
            name='PlainTextAsset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('handle', models.CharField(max_length=48)),
                ('text', models.TextField(default='')),
                ('site', models.ForeignKey(to='websites.Website')),
            ],
            bases=(models.Model, granite.core.objects.FSDuplicate),
        ),
    ]
