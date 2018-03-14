from django.conf.urls import url, include

from . import views

homepage_patterns = [
	url(r'^$', views.Index, name='index'),
]