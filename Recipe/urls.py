from django.conf.urls import patterns, include, url
from Recipe import views

urlpatterns = patterns('Recipe.views',
    url(r'^design/$',
        'recipe_design'),
    url(r'^hop/(?P<ing_id>\d+)/$',
        'get_hop'),
    url(r'^fermentable/(?P<ing_id>\d+)/$',
        'get_fermentable'),
    url(r'^yeast/(?P<ing_id>\d+)/$',
        'get_yeast'),
    #url(r'^view_recipe/(?<rec_id>\d+/$',
    #    'get_recipe'),
)
