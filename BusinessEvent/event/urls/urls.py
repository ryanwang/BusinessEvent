__author__ = 'lk'

from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'event.views.home'),
    url(r'^login$', 'event.small_views.user.login'),
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^register$', 'event.small_views.user.register'),
    url(r'^activate/(?P<user_email>.+)/(?P<random_id>.+)', 'event.small_views.user.activate'),
    url(r'^confirmation/$', 'event.small_views.user.confirmation'),
)