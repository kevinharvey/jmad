from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'solos.views.index'),
    url(r'^admin/', include(admin.site.urls)),
]
