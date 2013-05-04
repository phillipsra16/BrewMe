from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from Home_Screen.forms import UserRecipeForm
from Recipe.models import Recipe
from django.forms.formsets import formset_factory
from django.utils import simplejson

@login_required
def home(request):
    state = username = ''
    #Do some fun things
    if state == '':
        state = 'Welcome!'
        uid = request.session['user_id']
        username = User.objects.get(pk = uid).username


    return render_to_response('home.html', {
        'state' : state,
        'username' : username,
        }, context_instance=RequestContext(request))


def get_user_recipes(request):
    username = User.objects.get(id = request.session['user_id'])
    user_recipes = Recipe.objects.filter(user_id =
            request.session['user_id'])
    recipes_dict = []
    for recipe in user_recipes:
        r_dict = {
                "name"  : recipe.name,
                "style" : recipe.style_id.name,
                "id"    : recipe.id,
                }
        recipes_dict.append(r_dict)
    data = {
        "recipes" : recipes_dict
        }

    return HttpResponse(simplejson.dumps(data))
