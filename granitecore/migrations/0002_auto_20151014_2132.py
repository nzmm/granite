# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('granitecore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('brand_large', models.ForeignKey(to='granitecore.Asset', blank=True, related_name='branding_large')),
                ('brand_medium', models.ForeignKey(to='granitecore.Asset', blank=True, related_name='branding_medium')),
                ('brand_original', models.ForeignKey(to='granitecore.Asset', blank=True, related_name='branding_original')),
                ('brand_small', models.ForeignKey(to='granitecore.Asset', blank=True, related_name='branding_small')),
                ('favicon', models.ForeignKey(to='granitecore.Asset', blank=True, related_name='favicons')),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='mauthor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='mtime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 14, 21, 31, 40, 944448, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='publish_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 10, 14, 21, 31, 50, 720328, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='published',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 10, 14, 21, 31, 58, 752195, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='unpublish_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 10, 14, 21, 32, 6, 344522, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
