# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 04:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0031_auto_20170507_0407'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questioninstance',
            old_name='answer_weight',
            new_name='question_weight',
        ),
    ]