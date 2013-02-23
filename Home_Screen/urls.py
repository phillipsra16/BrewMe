from django.conf.urls import patterns, include, url

urlpatterns = patterns('Home_Screen.views',
    url(r'^$', 'home'),
)
