# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Tag(models.Model):
	nama = models.CharField(max_length=20, unique=True, null=True)
	slug = models.SlugField(unique=True, null=True)

	def __str__(self):
		return self.nama