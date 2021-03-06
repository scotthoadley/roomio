# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 00:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('matcher', '0053_auto_20170509_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrueMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_percent', models.FloatField(default=0)),
                ('user_onet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_onet', to=settings.AUTH_USER_MODEL)),
                ('user_twot', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_twot', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
