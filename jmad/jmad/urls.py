from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers

from albums.views import AlbumViewSet, TrackViewSet


router = routers.SimpleRouter()
router.register(r'albums', AlbumViewSet)
router.register(r'tracks', TrackViewSet)


urlpatterns = [

    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # API
    url(r'^api/', include(router.urls)),

    # Apps
    url(r'^recordings/(?P<album>[\w-]+)/(?P<track>[\w-]+)/(?P<artist>[\w-]+)/$',
        'solos.views.solo_detail', name='solo_detail_view'),
    url(r'^$', 'solos.views.index'),
]
