# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0006_auto_20170718_0342'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexerquery',
            name='source_filter_json',
            field=models.TextField(default=''),
        ),
    ]