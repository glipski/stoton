# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_website_template', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websitepost',
            name='category',
            field=models.CharField(choices=[('wydarzenia', 'wydarzenia'), ('informacje', 'informacje'), ('konkursy', 'konkursy'), ('wycieczki', 'wycieczki'), ('sport', 'sport')], max_length=80),
        ),
    ]
