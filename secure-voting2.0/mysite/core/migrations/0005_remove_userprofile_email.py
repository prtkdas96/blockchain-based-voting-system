# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-17 05:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
    ]
