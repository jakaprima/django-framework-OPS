from django.conf.urls import url, include

from . import views

homepage_patterns = [
	url(r'^$', views.Index.as_view(), name='index'),
	url(r'^(?P<tahun>[0-9]{4})/(?P<bulan>[0-9]{2})/(?P<artikelslug>[-\w]+)/$', views.Detail.as_view(), name='url-detailartikel'),
]