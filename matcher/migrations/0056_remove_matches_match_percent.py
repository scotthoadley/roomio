# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 02:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0055_auto_20170510_0209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matches',
            name='match_percent',
        ),
    ]
