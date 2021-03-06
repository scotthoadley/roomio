# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-10 18:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('matcher', '0056_remove_matches_match_percent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, max_length=500)),
                ('from_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='answers',
            name='answer_ideal',
            field=models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=1),
        ),
        migrations.AlterField(
            model_name='answers',
            name='answer_option',
            field=models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=1),
        ),
    ]
