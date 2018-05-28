# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-15 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180515_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.CharField(max_length=9999, verbose_name='内容'),
        ),
        migrations.RemoveField(
            model_name='article',
            name='tag',
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='users.Tag', verbose_name='标签'),
        ),
    ]