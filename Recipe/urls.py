from django.conf.urls import patterns, include, url
from ajax_select import urls as ajax_select_urls

urlpatterns = patterns('Recipe.views',
    url(r'^design/$', 'recipe_design'),
    url(r'^lookup/$', include(ajax_select_urls)),
)
