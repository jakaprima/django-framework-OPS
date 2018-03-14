# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import random
import os


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


# Create your models here.
class Produk(models.Model):
	nama_produk = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	deskripsi = models.TextField()
	harga = models.DecimalField(decimal_places=2, max_digits=20, default=50000.00)
	gambar = models.ImageField(upload_to=func_path_upload_gambar, null=True, blank=True)

	def __str__(self):
		return self.nama_produk

	def __unicode__(self):
		return self.nama_produk
