# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 13:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school_website_template', '0024_auto_20170128_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitepost',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='websitepost_update', to=settings.AUTH_USER_MODEL, verbose_name='last updated by'),
        ),
        migrations.AlterField(
            model_name='websitepost',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='websitepost_create', to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
    ]
