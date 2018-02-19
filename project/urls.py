from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, health

from homepage.urls import homepage_patterns
from homepage.views import Detail

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(homepage_patterns, namespace=
    "homepage", app_name="homepage")),
    url(r'^admin-panel/', include('adminapps.urls', namespace="admin-panel", app_name='admin-panel')),
    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
