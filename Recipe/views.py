from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django import forms

@login_required
def recipe_design(request):
    state = ''
    fermentation_form = hop_form = yeast_form = misc_form = ''

    # Data being submitted
    # This will either be via editing or creating a recipe
    if request.method == 'POST':
            fermentation_form = FermentationForm();
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
        if forms is not None:
            fermentation_form = request.GET#.get('fermentables','')
            hop_form = request.GET#.get('hops','')
            yeast_form = request.GET#.get('yeast','')
            misc_form = request.GET#.get('misc','')
        # Return blank forms
        else:
            fermentation_form = FermentationForm();
            hop_form = HopForm();
            yeast_form = YeastForm();
            misc_form = MiscForm();
    # Render above objects to a response and send it off
    return render_to_response('recipe_design.html', {
        'hop_form' : hop_form,
        'fermentation_form' : fermentation_form,
        'yeast_form' : yeast_form,
        'misc_form' : misc_form,
        }, context_instance=RequestContext(request))
