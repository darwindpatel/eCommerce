# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-04-06 07:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='prder_id',
            new_name='order_id',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='satus',
            new_name='status',
        ),
    ]
