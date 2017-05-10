# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 12:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0051_auto_20170509_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='matches',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='question', to='matcher.QuestionInstance'),
        ),
    ]
