from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django import forms
from django.template import RequestContext
from Recipe.forms import *
from Recipe.models import *

@login_required
def recipe_design(request):
    state = ''
    fermentable_form = hop_form = yeast_form = misc_form = ''

    # Data being submitted
    # This will either be via editing or creating a recipe,
    # or when we are filling out a form via 'onchange event' in the 
    # modelchoicefield
    if request.method == 'POST':
        fermentable_form = FermentationForm()
        hop_form = HopForm()
        #        name = request.POST.get('name',''))
        yeast_form = YeastForm()
        misc_form = MiscForm()
    # Set forms with pre-filled in data
    # Create a session and a new Recipe object
    # Check for null values in forms
    # If everything passes, submit Recipe object and redirect to display
    # Else reload with forms pre-filled in, highlight missing data

    # Data being requested
    # This will be when the user enters this view via recipe create or edit
    # or when the user fails to input all fields before a post
    # if request.method == 'GET':
    else:
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

    # Here's where we're handling the population of text fields from a selection
    # from a dropdown
    if request.method == 'GET':
        ingredient = request.GET.get('type', '')
        if ingredient == 'hop':
            hop_form = HopForm(request.GET)
            hop_object = Hop.objects.get(name=hop_form['name'])
            hop_form['use'] = hop_object.use
            hop_form['alpha'] = hop_object.alpha_acid

    # Render above objects to a response and send it off
    return render_to_response('recipe.html', {
        'hop_form' : hop_form,
        'fermentable_form' : fermentable_form,
        'yeast_form' : yeast_form,
        'misc_form' : misc_form,
        'state' : state,
        }, context_instance=RequestContext(request))
