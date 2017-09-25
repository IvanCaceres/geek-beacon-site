# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-25 02:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_menuitem_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.MenuItem'),
        ),
    ]