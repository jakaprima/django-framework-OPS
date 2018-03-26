from django.conf.urls import url, include

from .views import index, detail

urlpatterns = [
	url(r'^$', index, name="index"),
	url(r'^detail/(?P<nama_produk_slug>[-\w]+)/$', detail, name="detail"),
	url(r'^keranjang/', include('keranjang.urls', namespace="keranjang")),
]

