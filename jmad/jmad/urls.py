from django.conf.urls import patterns, include, url
from django.contrib import admin

from solos.views import SoloDetailView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^solos/(?P<pk>\d+)/$', SoloDetailView.as_view()),
    url(r'^$', 'solos.views.index'),
)
