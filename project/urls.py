from django.conf import settings
from  django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin

from homepage.urls import homepage_patterns
from blog.urls import blog_patterns
from blog.views import Detail
from welcome.views import health



urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(homepage_patterns, namespace="homepage", app_name="homepage")),
    url(r'^akun/', include('akun.urls', namespace="akun")),
    url(r'^pencarian', include('pencarian.urls', namespace='pencarian', app_name='pencarian')),
    url(r'^blog/', include(blog_patterns, namespace="blog", app_name="blog")),
    url(r'^shop/', include('jualbeliapp.urls', namespace="jualbeli", app_name="jualbeli")),
    url(r'^admin-panel/', include('adminapps.urls', namespace="admin-panel", app_name='admin-panel')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^health$', health),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
