# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-20 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_dbldap_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbldap',
            name='is_authenticated',
            field=models.BooleanField(default=False),
        ),
    ]