# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-06 12:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miner', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='user',
        ),
    ]
