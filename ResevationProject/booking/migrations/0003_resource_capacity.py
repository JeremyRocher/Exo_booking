# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-30 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20180930_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='capacity',
            field=models.IntegerField(default=1),
        ),
    ]