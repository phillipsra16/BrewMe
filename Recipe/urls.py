from django.conf.urls import patterns, include, url
from Recipe import views

urlpatterns = patterns('Recipe.views',
    url(r'^design/$', 'recipe_design'),
)
