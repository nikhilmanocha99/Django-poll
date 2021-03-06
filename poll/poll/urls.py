from django.conf.urls import patterns, include, url


from django.contrib import admin
from register.views import *

admin.autodiscover()

urlpatterns = patterns('',
                url(r'^admin/', include(admin.site.urls)),
                url(r'^polls/', include('main.urls', namespace='polls')),
                url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                url(r'^register/', register),
)
