# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('domain', models.CharField(max_length=100, default='http://127.0.0.1:8000/')),
                ('handle', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=255, default='')),
                ('authors', models.CharField(blank=True, max_length=255, default='')),
                ('copyright', models.CharField(blank=True, max_length=255, default='')),
            ],
        ),
    ]
