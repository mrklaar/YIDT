# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-23 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YIDT_app', '0002_auto_20180923_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='Img',
            field=models.CharField(max_length=264),
        ),
    ]
