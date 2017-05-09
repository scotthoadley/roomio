# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0041_auto_20170507_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='answer_weight',
            field=models.CharField(choices=[('1', 'Not Important At all'), ('25', 'Somewhat Important'), ('150', 'Very Important'), ('250', 'Mandatory')], default='1', help_text='Answer Weighting', max_length=3),
        ),
    ]