# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-05-15 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostmodel',
            name='disk_capacity',
            field=models.FloatField(blank=True, null=True, verbose_name='磁盘容量(单位Gb)'),
        ),
    ]
