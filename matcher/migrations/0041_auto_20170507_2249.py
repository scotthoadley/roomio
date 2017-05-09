# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 22:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0040_auto_20170507_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='question_id',
        ),
        migrations.AddField(
            model_name='answers',
            name='question',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='matcher.QuestionInstance'),
        ),
    ]