# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artikel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('judul_artikel', models.CharField(max_length=200)),
                ('isi_artikel', ckeditor.fields.RichTextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama_kategori', models.CharField(max_length=25)),
                ('slug', models.SlugField(unique=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Komentar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isi_komentar', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(null=True, blank=True)),
                ('artikel', models.ForeignKey(blank=True, to='homepage.Artikel', null=True)),
                ('penulis_komentar', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Penulis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='SettingWeb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama_web', models.CharField(max_length=35)),
                ('deskripsi_web', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='artikel',
            name='kategori_artikel',
            field=models.ForeignKey(related_name='kategori_related', blank=True, to='homepage.Kategori', null=True),
        ),
        migrations.AddField(
            model_name='artikel',
            name='penulis',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
