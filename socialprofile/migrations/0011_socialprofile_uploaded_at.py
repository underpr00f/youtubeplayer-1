# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-12 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialprofile', '0010_auto_20170212_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialprofile',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
