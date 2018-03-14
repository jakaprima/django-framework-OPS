# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-12 02:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('artikel', '0002_artikel_publish_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikel',
            name='tag_artikel',
            field=models.ManyToManyField(blank=True, null=True, related_name='tag_related', to='tags.Tag'),
        ),
    ]
