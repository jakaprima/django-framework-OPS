# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from django.views.generic import TemplateView, UpdateView, DeleteView

from .models import Artikel
from kategori.models import Kategori
from django.db.models import Count

# Create your views here.

class ArtikelList(TemplateView):
	template_name = 'adminapps/adm_dashboard/semuapost.html'
	def get_context_data(self, **kwargs):
	    context = super(ArtikelList, self).get_context_data(**kwargs)
	    queryset = Artikel.objects.select_related().annotate(komentar_count=Count('komentar'))

	    # print queryset[0].komentar_count
	    # print queryset.query
	    # "homepage_artikel"."id",
	    # "homepage_artikel"."penulis_id",
	    # "homepage_artikel"."judul_artikel",
	    # "homepage_artikel"."kategori_artikel_id",
	    # "homepage_artikel"."isi_artikel",
	    # COUNT("homepage_komentar"."id") AS "komentar_count" FROM "homepage_artikel" LEFT OUTER JOIN "homepage_komentar" ON ( "homepage_artikel"."id" = "homepage_komentar"."artikel_id" ) GROUP BY "homepage_artikel"."id", "homepage_artikel"."penulis_id", "homepage_artikel"."judul_artikel", "homepage_artikel"."kategori_artikel_id", "homepage_artikel"."isi_artikel"

	    context = {
	    	'data_artikel': queryset,
	    }
	    return context

class EditArtikel(UpdateView):
	model = Artikel
	fields = ['judul_artikel', 'isi_artikel']
	template_name = 'adminapps/artikel_update_form.html'
	# template_name_suffix = '_halo_form' #artikel_update_form
	def form_valid(self, form):
		artikel = form.save(commit=False)
		artikel.updated_at = timezone.now()
		artikel.save()
		list_kategori_input = self.request.POST.getlist('kategori_input')
		kategori_artikel_id = list(artikel.kategori_artikel.values_list('id', flat=True))

		for id in kategori_artikel_id:
			artikel.kategori_artikel.remove(id)
			artikel.save()

		for id in list_kategori_input:
			artikel.kategori_artikel.add(id)
			artikel.save()
		return redirect('admin-panel:url-listpost')

	def get_context_data(self, **kwargs):
	    context = super(EditArtikel, self).get_context_data(**kwargs)
	    context['data_kategori'] = Kategori.objects.all()
	    return context

class DeleteArtikel(DeleteView):
	template_name = 'adminapps/artikel_confirm_delete.html'
	model = Artikel
	success_url = reverse_lazy('admin-panel:url-listpost')

