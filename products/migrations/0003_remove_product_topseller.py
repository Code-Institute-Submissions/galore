# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-02 21:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200121_1009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='topseller',
        ),
    ]