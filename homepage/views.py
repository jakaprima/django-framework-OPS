from django.shortcuts import render
from django.views.generic import TemplateView

from .models import SettingWeb, Artikel
# Create your views here.


class Index(TemplateView):
	template_name = 'homepage/index.html'
	def get_context_data(self, **kwargs):
	    context = super(Index, self).get_context_data(**kwargs)
	    queryset = SettingWeb.objects.first()
	    queryset_artikel = Artikel.objects.all()
	    context['data_setting_web'] = queryset
	    context['data_artikel'] = queryset_artikel
	    return context


