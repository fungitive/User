# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-29 08:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20180529_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(default='./upload/article/common.jpg', help_text='大小200*200，不超过200k', null=True, upload_to='./upload/article/', verbose_name='缩略图'),
        ),
    ]
