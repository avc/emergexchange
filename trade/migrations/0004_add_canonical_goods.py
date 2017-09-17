# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 04:04
from __future__ import unicode_literals

from django.db import migrations
from django.utils.text import slugify

SLUG_LENGTH = 63

CANONICAL_GOODS = [ 'canned food', 'water', 'gas', 'blanket', 'shoes', 'shirt', 'jacket', 'tent', 'lighter', 'flashlight',
    'pants', 'rubbing alcohol', 'gauze', 'towel', 'cookware', 'dishes', 'forks', 'car', 'bicycle', ]

def add_canonical_goods(apps, schema_editor):
    CanonicalGood = apps.get_model('trade', 'CanonicalGood')
    for good_name in CANONICAL_GOODS:
        new_good = CanonicalGood.objects.create(
            name=good_name,
            slug=slugify(good_name))

def remove_canonical_goods(apps, schema_editor):
    CanonicalGood = apps.get_model('trade', 'CanonicalGood')
    for good_name in CANONICAL_GOODS:
        good = CanonicalGood.objects.get(name=good_name)
        good.delete()

class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0003_auto_20170917_0341'),
    ]

    operations = [
        migrations.RunPython(
            add_canonical_goods,
            remove_canonical_goods)
    ]