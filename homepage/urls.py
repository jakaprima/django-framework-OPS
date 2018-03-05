from django.conf.urls import url, include

from . import views

homepage_patterns = [
	url(r'^$', views.Index, name='index'),
	url(r'^daftar/$', views.Daftar.as_view(), name='daftar'),
	url(r'^(?P<tahun>[0-9]{4})/(?P<bulan>[0-9]{2})/(?P<artikelslug>[-\w]+)/$', views.Detail.as_view(), name='url-detailartikel'),
	url(r'^session/$', views.keranjang, name="keranjang"),
	# url(r'^tentang-kami/$', views.tentangkami, name="tentang-kami"),
	url(r'^tentang-kami/$', views.TentangKami.as_view(), name="tentang-kami"),
]