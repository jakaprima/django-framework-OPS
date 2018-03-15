# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import random
import os

from django.db.models import Q


def ambil_extensi_nama_file(filepath):
	base_name = os.path.basename(filepath)
	nama, ext = os.path.splitext(base_name)
	return nama, ext

def func_path_upload_gambar(instance, filename):
	# print instance
	# print fileName
	nama_filebaru = random.randint(1,3910209312)
	nama, ext = ambil_extensi_nama_file(filename)
	nama_file_final = '{nama_filebaru}{ext}'.format(nama_filebaru=nama_filebaru, ext=ext)
	return "produk/{nama_filebaru}/{nama_file_final}".format(nama_filebaru=nama_filebaru, nama_file_final=nama_file_final)


class ProdukQuerySet(models.query.QuerySet):
	def cariquery(self, query):
		data = (Q(nama_produk__icontains=query)
			)
		return self.filter(data).distinct()

class ProdukManager(models.Manager):
	#kalo mau gunain models.query.QuerySet
	def get_queryset(self):
		return ProdukQuerySet(self.model, using=self._db)
	#kalo mau gunain queryset
	def semua(self):
		return self.get_queryset()
	def cari(self, query):
		return self.get_queryset().cariquery(query)



# Create your models here.
class Produk(models.Model):
	nama_produk = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	deskripsi = models.TextField()
	harga = models.DecimalField(decimal_places=2, max_digits=20, default=50000.00)
	gambar = models.ImageField(upload_to=func_path_upload_gambar, null=True, blank=True)

	objects = ProdukManager()

	def __str__(self):
		return self.nama_produk

	def __unicode__(self):
		return self.nama_produk
