from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^recordings/(?P<album>[\w-]+)/(?P<track>[\w-]+)/(?P<artist>[\w-]+)/$',
        'solos.views.solo_detail', name='solo_detail_view'),
    url(r'^$', 'solos.views.index'),
    url(r'^admin/', include(admin.site.urls)),
]
