from django.shortcuts import render_to_response
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

    # Data being requested
    # This will be when the user enters this view via recipe create or edit
    # or when the user fails to input all fields before a post
    # if request.method == 'GET':
    state = 'get'
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
        'state' : state,
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
                    'alpha_acid'    : str(hop.alpha_acid),}
        return HttpResponse(simplejson.dumps(hop_dict))


def get_yeast(request, ing_id):
    # Data being submitted
    # This will either be via editing or creating a recipe,
    # or when we are filling out a form via 'onchange event' in the 
    # modelchoicefield
    if request.method == 'GET':
        yeast = Yeast.objects.get(pk = ing_id)
        yeast_dict= { 'yeast_name'      : str(yeast.description),
                      'description'     : str(yeast.name),
                      'flocculation'    : str(yeast.flocculation),
                      'attenuation'     : str(yeast.attenuation),}
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
                     'description'      : str(ferm.description),}
        return HttpResponse(simplejson.dumps(ferm_dict))

def get_recipe(request, rec_id):
    if request.method == 'GET':
        recipe_dict = { 'recipe_name'   : str(Recipe.objects.get(pk = rec_id)),
                        'hop_schedule'  : get_hop_schedule(rec_id),
                        'grain_bill'    : get_grain_bill(rec_id),
                        'yeast'         : get_yeast_for_recipe(rec_id),
                        'misc'          : get_misc_for_recipe(rec_id)}
#        return HttpResponse(simplejson.dumps(recipe_dict))
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
        grain = Fermentable.objects.get(name = entry.fermentable_id)
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
    yeast = Yeast.objects.get(pk = Recipe.objects.get(pk = rec_id).yeast_id)
    yeast_dict = { 'name'           : yeast.name,
                   'description'    : yeast.description,
                   'flocculation'   : yeast.flocculation,
                   'attenuation'    : yeast.attenuation}
    return yeast_dict
