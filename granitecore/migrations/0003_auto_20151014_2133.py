# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('granitecore', '0002_auto_20151014_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='brand_large',
            field=models.ForeignKey(blank=True, to='granitecore.Asset', related_name='branding_large', null=True),
        ),
        migrations.AlterField(
            model_name='website',
            name='brand_medium',
            field=models.ForeignKey(blank=True, to='granitecore.Asset', related_name='branding_medium', null=True),
        ),
        migrations.AlterField(
            model_name='website',
            name='brand_original',
            field=models.ForeignKey(blank=True, to='granitecore.Asset', related_name='branding_original', null=True),
        ),
        migrations.AlterField(
            model_name='website',
            name='brand_small',
            field=models.ForeignKey(blank=True, to='granitecore.Asset', related_name='branding_small', null=True),
        ),
        migrations.AlterField(
            model_name='website',
            name='favicon',
            field=models.ForeignKey(blank=True, to='granitecore.Asset', related_name='favicons', null=True),
        ),
    ]
