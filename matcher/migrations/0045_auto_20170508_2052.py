# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0044_auto_20170508_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='answer_weight',
            field=models.CharField(choices=[('0', 'Not Important At all'), ('1', 'Somewhat Important'), ('10', 'Very Important'), ('250', 'Mandatory')], default='1', help_text='Answer Weighting', max_length=3),
        ),
    ]
