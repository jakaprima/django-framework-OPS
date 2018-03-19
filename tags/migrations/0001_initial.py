# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-12 01:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=20, null=True, unique=True)),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
        ),
    ]