# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-25 23:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_remove_courseorg_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='name',
            field=models.CharField(default='全国知名', max_length=10, verbose_name='机构标签'),
        ),
    ]