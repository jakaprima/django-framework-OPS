# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models

from product.models import Produk
from core.models import TimeStampedModel

User = settings.AUTH_USER_MODEL



class KeranjangManager(models.Manager):
	def baru_atau_get(self, request):
		keranjang_id = request.session.get("keranjang_id", None)
		qs = self.get_queryset().filter(id=keranjang_id)
		if qs.count() == 1:
			new_obj = False
			keranjang_obj = qs.first()
			if request.user.is_authenticated() and keranjang_obj.user is None:
				keranjang_obj.user = request.user
				keranjang_obj.save()
		else:
			keranjang_obj = Keranjang.objects.new(user=request.user)
			new_obj = True
			request.session['keranjang_id'] = keranjang_obj.id
		return keranjang_obj, new_obj

	def baru(self, user=None):
		user_obj = None
		if user is not None:
			if user.is_authenticated():
				user_obj = user
		return self.model.objects.Create(user=user_obj)

# Create your models here.
class Keranjang(TimeStampedModel):
	user = models.ForeignKey(User, null=True, blank=True)
	produk = models.ManyToManyField(Produk, blank=True)
	subtotal = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

	objects = KeranjangManager()

	def __str__(self):
		return str(self.id)

