from django.conf.urls import patterns, include, url
from Channeladmin.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^Register/$',Register,name="register"),
    url(r'^Login/$',Login,name="Login"),
    url(r'^Index/$',Index,name="Index"),
    url(r'^Logout/$',Logout,name="Logout"),


    url(r'^admin/', include(admin.site.urls)),
)

