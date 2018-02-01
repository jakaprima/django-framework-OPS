from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^$', views.Index.as_view()),
	url(r'^(?P<artikelslug>[-\w]+)$', views.Detail.as_view(), name='url-detailartikel'),
]