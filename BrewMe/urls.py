from django.conf.urls.default import *
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('User_Auth.urls')),
    url(r'^user/', include('User_Auth.urls')),
    url(r'^home/', include('Home_Screen.urls')),
    url(r'^recipe/', include('Recipe.urls')),
)
