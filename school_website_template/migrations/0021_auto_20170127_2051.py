# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_website_template', '0020_auto_20170127_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websitepost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='website_posts_images/%Y/%m/%d'),
        ),
    ]