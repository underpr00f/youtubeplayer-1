# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-13 00:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0011_auto_20170812_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberaccept',
            name='agree',
            field=models.BooleanField(default=False),
        ),
    ]