# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_website_template', '0019_auto_20170127_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.ImageField(upload_to='gallery/%Y/%m/%d'),
        ),
    ]