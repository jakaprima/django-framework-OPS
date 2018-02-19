# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20180213_0213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artikel',
            name='kategori_artikel',
        ),
        migrations.AddField(
            model_name='artikel',
            name='kategori_artikel',
            field=models.ManyToManyField(related_name='kategori_related', null=True, to='homepage.Kategori', blank=True),
        ),
    ]
