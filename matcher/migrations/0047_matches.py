# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0046_auto_20170508_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_one', models.IntegerField(default=0)),
                ('user_two', models.IntegerField(default=0)),
                ('match_percent', models.IntegerField(default=0)),
            ],
        ),
    ]
