# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from product.models import Produk

# Create your views here.
def index(request):
	context = {
		'data_produk': Produk.objects.all()
	}
	return render(request, 'jualbeliapp/index.html', context)

def detail(request, nama_produk_slug=None):
	qs = get_object_or_404(Produk, slug=nama_produk_slug)
	context = {
		'data_produk': qs
	}
	return render(request, 'jualbeliapp/detail.html', context)
