from django.conf.urls import url, include

from .views import index, update

urlpatterns = [
	url(r'^', index, name="index"),
	url(r'^keranjang-update', update, name="update")
]