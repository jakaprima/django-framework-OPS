# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models

from product.models import Produk
from core.models import TimeStampedModel

# User = settings.AUTH_USER_MODEL

# Create your models here.
class Keranjang(TimeStampedModel):
	# user = models.ForeignKey(User, null=True, blank=True)
	produk = models.ManyToManyField(Produk, blank=True)
	subtotal = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	def __str__(self):
		return str(self.id)

