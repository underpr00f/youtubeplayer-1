# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-10 19:54
from __future__ import unicode_literals

from django.db import migrations, models
import socialprofile.models


class Migration(migrations.Migration):

    dependencies = [
        ('socialprofile', '0007_socialprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=socialprofile.models.avatar_upload_to, verbose_name='Загрузка аватара'),
        ),
    ]
