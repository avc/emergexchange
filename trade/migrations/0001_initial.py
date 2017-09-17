# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 00:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CanonicalGood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63, unique=True)),
                ('slug', models.SlugField(max_length=63, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('modified', models.DateField(auto_now=True)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trade.CanonicalGood')),
            ],
        ),
        migrations.CreateModel(
            name='Need',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField()),
                ('modified', models.DateField(auto_now=True)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trade.CanonicalGood')),
            ],
        ),
    ]
