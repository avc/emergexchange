# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 06:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0011_auto_20170917_0618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='need',
            old_name='detail',
            new_name='description',
        ),
    ]
