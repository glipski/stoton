# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_website_template', '0023_delete_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
