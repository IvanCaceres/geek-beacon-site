# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-24 10:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20170924_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published_at',
        ),
    ]