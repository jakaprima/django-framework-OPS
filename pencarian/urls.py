from django.conf.urls import url
from .views import pencarianview

urlpatterns = [
	url(r'^$', pencarianview, name='index')
]