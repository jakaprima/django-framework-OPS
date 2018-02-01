from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.http import HttpResponse

from .models import SettingWeb, Artikel, Komentar

from django.utils.text import slugify
from django.db import connection
from .forms import KomentarForm
# Create your views here.


class Index(TemplateView):
	template_name = 'homepage/index.html'
	def get_context_data(self, **kwargs):
	    context = super(Index, self).get_context_data(**kwargs)
	    queryset = SettingWeb.objects.first()
	    queryset_artikel = Artikel.objects.all().order_by('-created_at')

	    context['data_setting_web'] = queryset
	    context['data_artikel'] = queryset_artikel
	    return context


class Detail(TemplateView):
	form_class = KomentarForm()
	template_name = 'homepage/detail.html'
	def get_context_data(self, artikelslug=None, *args, **kwargs):
		context = super(Detail, self).get_context_data(**kwargs)
		a = artikelslug.replace('-', ' ')
		queryset_artikel = Artikel.objects.get(judul_artikel__contains=a)
		queryset_komentar = Komentar.objects.filter(artikel__judul_artikel__contains=a)

		form_class = KomentarForm()

		queryset = SettingWeb.objects.first()
		context = {
			'data_artikel': queryset_artikel,
			'data_setting_web': queryset,
			'data_komentar': queryset_komentar,
			'form_class': form_class,
		}
		return context




