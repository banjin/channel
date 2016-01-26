from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^channeladmin/', include('Channeladmin.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
