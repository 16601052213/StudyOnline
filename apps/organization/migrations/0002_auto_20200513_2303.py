# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-13 23:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='category',
            field=models.CharField(choices=[('pxjg', '培训机构'), ('gr', '个人'), ('gx', '高校')], default='pxjg', max_length=20, verbose_name='机构类别'),
        ),
        migrations.AlterField(
            model_name='citydict',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间'),
        ),
    ]