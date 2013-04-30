from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.template import RequestContext
from Recipe.forms import *
from Recipe.models import *
from django.utils import simplejson
import json

@login_required
@never_cache
def recipe_design(request):
    state = ''
    fermentable_form = hop_form = yeast_form = misc_form = ''

    # Set forms with pre-filled in data
    # Create a session and a new Recipe object
    # Check for null values in forms
    # If everything passes, submit Recipe object and redirect to display
    # Else reload with forms pre-filled in, highlight missing data

    if request.method == 'POST':
        # incoming data is not sanitized,
        # TODO: write sanitizer, put in Recipe/models.py:Recipe.__init__

        # Gather the info we need for recipe creation
        user_id = request.session['user_id']
        recipe_dict = simplejson.loads( request.POST.get('msg', ''))
        print(recipe_dict)

        # TODO: encapsulate these into individual methods
        # TODO: DEPENDENT ON TODO IN recipe.html, parse ingredients by names 
        #       instead of ids
        # Recipe creation
        my_recipe = Recipe()
        my_recipe.user_id      = User.objects.get(id = user_id)
        my_recipe.name         = recipe_dict['meta']['recipe_name']
        my_recipe.yeast_id     = Yeast.objects.get(name =
                                        recipe_dict['yeast']['name'])
        my_recipe.style_id     = Style.objects.get(name = 'test')
        my_recipe.save()

        # Grain Bill creation
        for ferm in recipe_dict['fermentable']:
            my_grain                = GrainBill()
            my_grain.recipe_id      = my_recipe
            # workaround for no first() in django queryset api
            my_grain.fermentable_id = Fermentable.objects.get(pk = ferm['id'])
            my_grain.amount         = ferm['amount']
            my_grain.use            = ferm['use']
            my_grain.save()

        for hop in recipe_dict['hop']:
            my_hop              = HopSchedule()
            my_hop.recipe_id    = my_recipe
            my_hop.hop_id       = Hop.objects.get(pk = hop['id'])
            my_hop.time         = hop['time']
            my_hop.amount       = hop['amount']
            my_hop.use          = hop['use']
            my_hop.save()

        return HttpResponse(simplejson.dumps({'url' : '/recipe/view_recipe/%s/'
                % my_recipe.id}))

    # Data being requested
    # This will be when the user enters this view via recipe create or edit
    # or when the user fails to input all fields before a post
    # if request.method == 'GET':
    # Check if we need to prefill forms
    method = request.GET.get('method', '')

    # Pre fill forms
    if method == 'edit':
        fermentable_form = request.GET#.get('fermentables','')
        hop_form = request.GET#.get('hops','')
        yeast_form = request.GET#.get('yeast','')
        misc_form = request.GET#.get('misc','')
    # Return blank forms
    else:
        fermentable_form = FermentableForm()
        hop_form = HopForm()
        yeast_form = YeastForm()
        misc_form = MiscForm()

    # Render above objects to a response and send it off
    return render_to_response('recipe.html', {
        'hop_form' : hop_form,
        'fermentable_form' : fermentable_form,
        'yeast_form' : yeast_form,
        'misc_form' : misc_form,
        }, context_instance=RequestContext(request))


def get_hop(request, ing_id):
    # Data being submitted
    # This will either be via editing or creating a recipe,
    # or when we are filling out a form via 'onchange event' in the 
    # modelchoicefield
    if request.method == 'GET':
        hop = Hop.objects.get(pk = ing_id)
        hop_dict= { 'use'           : str(hop.use),
                    'hop_name'      : str(hop.name),
                    'description'   : str(hop.description),
                    'alpha_acid'    : str(hop.alpha_acid),
                    'id'            : str(hop.id),}
        return HttpResponse(simplejson.dumps(hop_dict))


def get_yeast(request, ing_id):
    # Data being submitted
    # This will either be via editing or creating a recipe,
    # or when we are filling out a form via 'onchange event' in the 
    # modelchoicefield
    if request.method == 'GET':
        yeast = Yeast.objects.get(pk = ing_id)
        yeast_dict= { 'yeast_name'      : str(yeast.name),
                      'description'     : str(yeast.description),
                      'flocculation'    : str(yeast.flocculation),
                      'attenuation'     : str(yeast.attenuation),
                      'id'              : str(yeast.id),}
        return HttpResponse(simplejson.dumps(yeast_dict))


def get_fermentable(request, ing_id):
    # Data being submitted
    # This will either be via editing or creating a recipe,
    # or when we are filling out a form via 'onchange event' in the 
    # modelchoicefield
    if request.method == 'GET':
        ferm = Fermentable.objects.get(pk = ing_id)
        ferm_dict= { 'fermentable_name' : str(ferm.name),
                     'color'            : str(ferm.color),
                     'potential'        : str(ferm.potential_extract),
                     'use'              : str(ferm.use),
                     'description'      : str(ferm.description),
                     'id'               : str(ferm.id),}
        return HttpResponse(simplejson.dumps(ferm_dict))


@never_cache
def get_recipe(request, rec_id):
    recipe_dict = { 'recipe_name'   : str(Recipe.objects.get(pk = rec_id)),
                    'hop_schedule'  : get_hop_schedule(rec_id),
                    'grain_bill'    : get_grain_bill(rec_id),
                    'yeast'         : get_yeast_for_recipe(rec_id),
                    'misc'          : get_misc_for_recipe(rec_id)}
    #return HttpResponse(simplejson.dumps(recipe_dict))
    return render_to_response('view_recipe.html', {
        'recipe_dict' : simplejson.dumps(recipe_dict),
        }, context_instance=RequestContext(request))


def get_hop_schedule(rec_id):
    # We need a hop schedule for a given recipe
    # This gets all of the hops and information for a given recipe id
    # and returns a dictionary of lists with all of the information
    # needed to reconstruct the hop schedule
    hop_sched = HopSchedule.objects.filter(recipe_id = rec_id)
    hop_sched_list = []

    for entry in hop_sched:
        hop = Hop.objects.get(name = entry.hop_id)
        hop_dict = { 'name'         : hop.name,
                     'alpha_acid'   : str(hop.alpha_acid),
                     'time'         : entry.time,
                     'amount'       : str(entry.amount),
                     'use'          : entry.use}
        hop_sched_list.append(hop_dict)
    return hop_sched_list


def get_grain_bill(rec_id):
    # This will return a list of all of the grains that are being used
    # for a particular recipe
    grain_bill = GrainBill.objects.filter(recipe_id = rec_id)
    grain_list = []

    for entry in grain_bill:
        # Workaround
        # TODO: FIX THE FUCKIN DATABASE!!!  
        grain_set = list(Fermentable.objects.filter(name = entry.fermentable_id))
        grain = grain_set[0]
        grain_dict = { 'name'       : grain.name,
                       'color'      : grain.color,
                       'ppg'        : str(grain.potential_extract),
                       'amount'     : str(entry.amount),
                       'use'        : entry.use}
        grain_list.append(grain_dict)
    return grain_list


def get_misc_for_recipe(rec_id):
    misc_stuff = MiscBill.objects.filter(recipe_id = rec_id)
    misc_list = []

    for entry in misc_stuff:
        misc = Misc.objects.get(name = entry.misc_id)
        misc_dict = {   'name'      : misc.name,
                        'descr'     : misc.description}
        misc_list.append(misc_dict)

    return misc_list


def get_yeast_for_recipe(rec_id):
    # This gets the yeast associated with a particular recipe.
    yeast_id = Recipe.objects.get(pk = rec_id).yeast_id
    print(yeast_id)
    yeast = Yeast.objects.get(name = yeast_id)
    yeast_dict = { 'name'           : yeast.name,
                   'description'    : yeast.description,
                   'flocculation'   : yeast.flocculation,
                   'attenuation'    : yeast.attenuation}
    return yeast_dict


def search_recipes(request):
    recipes = 'Nothing Found'
    search_term = request.GET.get('q','')
    if query:
        results = SearchQuerySet().auto_query(search_term)
        recipes = []
        for r in recipes:
            recipes.append(r.object)
    return HttpResponse(recipes)
