# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from artikel.models import Artikel

from core.models import TimeStampedModel

# Create your models here.
class Komentar(TimeStampedModel):
	artikel = models.ForeignKey(Artikel, blank=False)
	penulis_komentar = models.CharField(max_length=255, blank=False)
	email = models.EmailField(max_length=50, blank=False)
	isi_komentar = models.CharField(max_length=200, blank=False)
	publish_status = models.BooleanField(default=False)

	def __str__(self):
		return self.isi_komentar
		# return '(artikel) '+ str(self.artikel) + ' (komentar) ' + str(self.isi_komentar)

