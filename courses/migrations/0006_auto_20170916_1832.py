# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-16 18:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_lecture_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lecture',
            options={'ordering': ['-order', '-title']},
        ),
    ]
