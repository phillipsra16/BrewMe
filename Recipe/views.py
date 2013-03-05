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
    # This will either be via editing or creating a recipe
    if request.method == 'POST':
            fermentable_form = FermentationForm();
            hop_form = HopForm();
            yeast_form = YeastForm();
            misc_form = MiscForm();
        # Set forms with pre-filled in data
        # Create a session and a new Recipe object
        # Check for null values in forms
        # If everything passes, submit Recipe object and redirect to display
        # Else reload with forms pre-filled in, highlight missing data

    # Data being requested
    # This will be when the user enters this view via recipe create or edit
    # or when the user fails to input all fields before a post
    if request.method == 'GET':
        # Check if we need to prefill forms
        forms = request.GET.get('form', '')
        # Pre fill forms
        if forms:
            fermentable_form = request.GET#.get('fermentables','')
            hop_form = request.GET#.get('hops','')
            yeast_form = request.GET#.get('yeast','')
            misc_form = request.GET#.get('misc','')
        # Return blank forms
        #else:
    fermentable_form = FermentableForm();
    hop_form = HopForm();
    if hop_form:
        state = 'form found'
    yeast_form = YeastForm();
    misc_form = MiscForm();
    # Render above objects to a response and send it off
    return render_to_response('recipe.html', {
        'hop_form' : hop_form,
        'fermentable_form' : fermentable_form,
        'yeast_form' : yeast_form,
        'misc_form' : misc_form,
        'state' : state,
        }, context_instance=RequestContext(request))
