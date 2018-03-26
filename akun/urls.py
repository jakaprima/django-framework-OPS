from django.conf.urls import url, include

from .views import daftar, akun_login, akun_logout, konfirmasi_akun, kirim_ulang_aktivasi

urlpatterns = [
	url(r'^daftar/', daftar, name="daftar"),
	url(r'^login/', akun_login, name="login"),
	url(r'^logout/', akun_logout, name="logout"),
	url(r'^email/konfirmasi/(?P<key>[0-9A-Za-z]+)/$', 
	        konfirmasi_akun, 
	        name='kirim-aktivasi'),
	url(r'^email/kirimulang/$', 
	        kirim_ulang_aktivasi, 
	        name='kirim-ulang-aktivasi'),
]