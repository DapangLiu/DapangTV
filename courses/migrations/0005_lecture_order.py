# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-16 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20170830_0447'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
