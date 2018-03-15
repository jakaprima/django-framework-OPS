# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from product.models import Produk


# Create your views here.
def pencarianview(request):
	# print request.GET.get('q')
	query = request.GET.get('q', None)
	if query is not None:
		data_produk = Produk.objects.cari(query)
	else:
		data_produk = Produk.objects.semua()

	context = {
		'data_produk': data_produk,
	}

	return render(request, 'pencarian/index.html', context)