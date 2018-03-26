# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'keranjang/index.html')

def update(request):
	print 'id', request.POST.get('produk_id')