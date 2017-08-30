# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_video_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='free',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='video',
            name='member_required',
            field=models.BooleanField(default=False),
        ),
    ]