# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 02:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0054_truematch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matches',
            name='total',
        ),
        migrations.AddField(
            model_name='matches',
            name='total_one',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='matches',
            name='total_two',
            field=models.IntegerField(default=0),
        ),
    ]
