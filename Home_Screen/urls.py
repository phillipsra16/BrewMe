from django.conf.urls import patterns, include, url
from Home_Screen import views

urlpatterns = patterns('Home_Screen.views',
    url(r'^$', 'home'),
    url(r'^user_recipes$', 'get_user_recipes')
)
