# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from kategori.models import Kategori
from tags.models import Tag

from tinymce.models import HTMLField
from core.models import TimeStampedModel

# Create your models here.
class ArtikelManager(models.Manager):
	def published(self, **kwargs):
		return self.filter(publish_status=True)


class Artikel(TimeStampedModel):
	penulis = models.ForeignKey(User, null=True, blank=True)
	judul_artikel = models.CharField(max_length=200)
	kategori_artikel = models.ManyToManyField(Kategori, null=True, blank=True, related_name='kategori_related') #biar bisa di pake di template
	# komentar_artikel = models.ManyToManyField('Komentar', blank=True, null=True, through='Postlist')
	tag_artikel = models.ManyToManyField(Tag, null=True, blank=True, related_name='tag_related')

	isi_artikel = HTMLField()
	publish_status = models.BooleanField(default=False)

	objects = ArtikelManager()

	# ----- fungsi action --------- #
	def tampilkan_post(self):
		self.published_date = timezone.now()
		self.save()

	def izin_komentar(self):
		return self.komentar.filter(izin_komentar=True)

	# ----- fungsi action --------- #
	def __str__(self): # biar di admin rownya tidak kata kata object tapi sesuai isi
		return str(self.judul_artikel)
