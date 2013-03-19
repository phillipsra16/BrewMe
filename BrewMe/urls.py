from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('User_Auth.urls')),
    url(r'^user/', include('User_Auth.urls')),
    url(r'^home/', include('Home_Screen.urls')),
    url(r'^recipe/', include('Recipe.urls')),
)
