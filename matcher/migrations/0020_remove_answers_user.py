# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 06:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0019_auto_20170505_0625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='user',
        ),
    ]
