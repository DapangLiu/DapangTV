# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20170828_0715'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
