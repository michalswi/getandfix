# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-16 13:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20161216_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dbldap',
            name='last_login',
        ),
    ]
