# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-29 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20180529_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(blank=True, default='./article/common.jpg', help_text='大小200*200，不超过200k', null=True, upload_to='./article/', verbose_name='缩略图'),
        ),
    ]
