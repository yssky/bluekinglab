# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-05-15 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0002_auto_20190515_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostmodel',
            name='ip',
            field=models.GenericIPAddressField(protocol='ipv4', verbose_name='ip地址'),
        ),
    ]