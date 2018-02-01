# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homepage', '0003_artikel'),
    ]

    operations = [
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
            ],
        ),
        migrations.AddField(
            model_name='artikel',
            name='penulis',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='komentar',
            name='artikel',
            field=models.ForeignKey(blank=True, to='homepage.Artikel', null=True),
        ),
        migrations.AddField(
            model_name='komentar',
            name='penulis_komentar',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='artikel',
            name='kategori_artikel',
            field=models.ForeignKey(related_name='kategori_related', blank=True, to='homepage.Kategori', null=True),
        ),
    ]
