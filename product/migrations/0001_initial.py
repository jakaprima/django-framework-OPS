# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-13 04:54
from __future__ import unicode_literals

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_produk', models.CharField(max_length=120)),
                ('slug', models.SlugField(unique=True)),
                ('deskripsi', models.TextField()),
                ('harga', models.DecimalField(decimal_places=2, default=50000.0, max_digits=20)),
                ('gambar', models.ImageField(blank=True, null=True, upload_to=product.models.func_path_upload_gambar)),
            ],
        ),
    ]
