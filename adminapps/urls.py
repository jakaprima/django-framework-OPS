from django.conf.urls import url 

from . import views
urlpatterns = [
	url(r'^$', views.Index.as_view(), name='url-adm-dashboard'),
	# url(r'^logout/$', views.LogoutView.as_view(), name="url-adm-logout"),
	url(r'^login/$', views.LoginView.as_view(), name="url-adm-login"),
]

	# url(r'^$', include('adm_dashboard.urls')),
	# url(r'^logout/$', views.LogoutView.as_view(), name="url-adm-logout"),
	# url(r'^login/$', views.LoginView.as_view(), name="url-adm-login"),
	# url(r'^listpost/$', views.SemuaPostView.as_view(), name='url-listpost'),
	# url(r'^tambahpost/$', views.TambahPostView.as_view(), name='url-tambahpost'),
	# url(r'^tutorialcbv/', include('app5cbv.urls')),