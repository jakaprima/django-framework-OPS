# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from product.models import Produk
from django.contrib.auth.models import User

# Create your views here.
def index(request):
	# print 'request user', request.user
	if  request.user.is_anonymous == True:
		data_user = 'Tamu'
	else:
		data_user = request.user

	# print 'halo', data_user_aja

	context = {
		'data_user': data_user,
		'data_produk': Produk.objects.all()
	}
	# print 'context', context
	return render(request, 'jualbeliapp/index.html', context)

def detail(request, nama_produk_slug=None):
	qs = get_object_or_404(Produk, slug=nama_produk_slug)
	context = {
		'data_produk': qs
	}
	return render(request, 'jualbeliapp/detail.html', context)

