# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 21:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0004_answers_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answers',
            old_name='answer',
            new_name='answer_weight',
        ),
        migrations.RenameField(
            model_name='questioninstance',
            old_name='question_answers',
            new_name='question_weights',
        ),
    ]
