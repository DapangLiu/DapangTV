# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 07:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='time_stamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=120),
            preserve_default=False,
        ),
    ]