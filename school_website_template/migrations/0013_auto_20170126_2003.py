# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_website_template', '0012_auto_20170126_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageingallery',
            name='image',
            field=models.ImageField(upload_to='gallery/'),
        ),
    ]
