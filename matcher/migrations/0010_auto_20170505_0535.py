# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 05:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0009_auto_20170505_0530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='answer_weight',
            field=models.CharField(choices=[('1', 'Not Important At all'), ('25', 'Somewhat Important'), ('150', 'Very Important'), ('250', 'Mandatory')], default='1', help_text='Answer Weighting', max_length=3),
        ),
        migrations.AlterField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='matcher.QuestionInstance', unique=True),
        ),
    ]
