from django.conf.urls import patterns, include, url
from Channeladmin.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'klb16.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^Login/$',Login,name="Login"),
    url(r'^Index/$',Index,name="Index"),


    url(r'^admin/', include(admin.site.urls)),
)
