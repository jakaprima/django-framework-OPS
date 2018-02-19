from django.conf.urls import url 

from . import views
urlpatterns = [
	url(r'^$', views.Index.as_view(), name='url-adm-dashboard'),
	# url(r'^logout/$', views.LogoutView.as_view(), name="url-adm-logout"),
	url(r'^login/$', views.LoginView.as_view(), name="url-adm-login"),
	url(r'^logout/$', views.LogoutView.as_view(), name="url-adm-logout"),
	url(r'^posts/$', views.ArtikelList.as_view(), name='url-listpost'),
	url(r'^tambahpost/$', views.TambahPostView.as_view(), name='url-tambahpost'),
	url(r'^tambahkategori/', views.TambahKategori.as_view(), name='url-tambahkategori'),
]

# url(r'^post/(?P<pk>\d+)$', views.ArtikelDetailView.as_view(), name='post_detail'),
# url(r'^post/new/$', views.CreateArtikelView.as_view(), name='post_new'),
# url(r'^post/(?P<pk>\d+)/edit/$', views.UpdateArtikelView.as_view(), name='post_edit'),
# url(r'^post/(?P<pk>\d+)/remove$',views.DeleteArtikelView.as_view(), name='post_remove'),
# url(r'^drafts/$',views.DraftListView.as_view(), name='post_draft_list'),
# url(r'^post/(?P<pk>\d+)/komentar/$', views.tambah_komentar_ke_post, name='tambah_komentar_ke_post'),
# url(r'^komentar/(?P<pk>\d+)/approve/$',views.komentar_diizinkan, name='komentar_diizinkan'),
# url(r'^komentar/(?P<pk>\d+)/remove/$', views.komentar_remove, name='komentar_remove'),
# url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),

# url(r'^$/daftar', views.DaftarView.as_view(), app_name='daftarApp')


	# url(r'^$', include('adm_dashboard.urls')),
	# url(r'^logout/$', views.LogoutView.as_view(), name="url-adm-logout"),
	# url(r'^login/$', views.LoginView.as_view(), name="url-adm-login"),
	# url(r'^listpost/$', views.SemuaPostView.as_view(), name='url-listpost'),
	# url(r'^tambahpost/$', views.TambahPostView.as_view(), name='url-tambahpost'),
	# url(r'^tutorialcbv/', include('app5cbv.urls')),