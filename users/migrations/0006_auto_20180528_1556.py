# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-28 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180515_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(max_length=9999, verbose_name='内容'),
        ),
    ]
