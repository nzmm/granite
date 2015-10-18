# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import granite.core.objects
import granite.validators


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('handle', models.CharField(validators=[granite.validators.validate_page_handle], max_length=100, default='/pages/')),
                ('page_description', models.CharField(blank=True, max_length=255, default='')),
                ('content', models.TextField(default='')),
                ('role', models.CharField(max_length=2, choices=[('NN', 'Standard Page'), ('HM', 'Home Page'), ('ER', 'Error Page')], default='NN')),
                ('quick_link', models.BooleanField(default=False)),
                ('mtime', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=True)),
                ('page_author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(to='websites.Website')),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('handle', models.CharField(max_length=48)),
                ('markup', models.TextField(default='')),
                ('site', models.ForeignKey(to='websites.Website')),
            ],
            bases=(models.Model, granite.core.objects.FSDuplicate),
        ),
        migrations.AddField(
            model_name='page',
            name='template',
            field=models.ForeignKey(to='pages.Template'),
        ),
    ]
