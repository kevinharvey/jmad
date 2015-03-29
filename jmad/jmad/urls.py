from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers

from albums.views import AlbumViewSet, TrackViewSet
from solos.views import SoloViewSet


router = routers.SimpleRouter()
router.register(r'albums', AlbumViewSet)
router.register(r'tracks', TrackViewSet)
router.register(r'solos', SoloViewSet)

urlpatterns = patterns('',

    # Django Admin
    url(r'^admin/', include(admin.site.urls)),

    # API
    url(r'^api/', include(router.urls)),

    # Apps
    url(r'^recordings/(?P<album>[\w-]+)/(?P<track>[\w-]+)/(?P<artist>[\w-]+)/$',
        'solos.views.solo_detail',
        name='solo_detail_view'),
    url(r'^$', 'solos.views.index'),
)
