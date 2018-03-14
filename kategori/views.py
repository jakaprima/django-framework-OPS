# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView

from .models import Kategori
from django.utils.text import slugify
from django.http import JsonResponse

# Create your views here.
class TambahKategori(TemplateView):
	def post(self, request, *args, **kwargs):
		input_kategori = request.POST.get('input_kategori')
		new_kategori = Kategori.objects.create(
			nama_kategori=input_kategori,
			slug=slugify(input_kategori),
		)
		new_kategori.save()
		return JsonResponse({'msg': '<tr><td><input type="checkbox" name="kategori_input" value="'+ str(new_kategori.id) +'"/> '+ input_kategori +'</td><tr>'})
