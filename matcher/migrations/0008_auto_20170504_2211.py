# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0007_answers_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answers',
            old_name='answer',
            new_name='answer_option',
        ),
        migrations.AlterField(
            model_name='questioninstance',
            name='question_option_1',
            field=models.CharField(default='Yes', max_length=200),
        ),
        migrations.AlterField(
            model_name='questioninstance',
            name='question_option_2',
            field=models.CharField(default='No', max_length=200),
        ),
    ]
