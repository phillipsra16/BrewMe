from django.conf.urls import patterns, include, url

urlpatterns = patterns('User_Auth.views',
    url(r'^$', 'user_login'),
    url(r'^create/$', 'user_create'),
    url(r'^logout/$', 'user_logout'),
    url(r'^settings/$', 'user_settings'),
)
