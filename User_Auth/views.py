# User_Authentication views
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.models import User
from django import forms
from User_Auth.forms import *
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# User login view
def user_login(request):
    #initialize all of the variables used to null
    state = username = password = ''

    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')

    #if view was called with POST request (log in was pressed)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        #set the username and password to use with Django's
        #built in authenticate method
        username = request.POST.get('username')
        password = request.POST.get('password')
        if password:
            password = password + \
                'and boom goes the dynamite'
        user = authenticate(username=username, password=password)

        # Handle the various cases
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['user_id'] = user.id
                return HttpResponseRedirect('/home/')
            else:
                state = "Your account is not active"

        else:
            state = "Username and/or Password incorrect"

    #if not called with post request
    if state == '':
        state = 'Please Log in'
        form = LoginForm()


    # Send back a response based on the context
    return render_to_response('user_login.html', {
        'state' : state,
        'username' : username,
        'form' : form
        }, context_instance=RequestContext(request))

def user_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/user')


def user_create(request):
    #Initialize relevant variables
    state = ''
    cont = True
    if request.method == 'POST':
        #Load our form
        form = RegistrationForm(request.POST)
        #Ensure Passwords match
        if form.data['password1'] == form.data['password2']:
            #Don't allow bad usernames
            try:
                form.clean_username()
            except:
                cont = False
            #Create our user object with Django ORM
            #and redirect to login page upon success
            if cont:
                user = User.objects.create_user(
                        username=form.data['username'],
                        password=form.data['password1'] + \
                        'and boom goes the dynamite',
                        email=form.data['email']
                        )
                return HttpResponseRedirect('/user/login/')
        else:
            state = "Passwords don't match"
    #If starting state
    else:
        state = 'Create an Account'
        form = RegistrationForm()
    #Render response based on intext
    return render_to_response('user_create.html', {
            'state' : state,
            'form' : form,
            }, context_instance=RequestContext(request))

@login_required
def user_settings(request):
    state = username = ''
    if request.method == 'POST':
        form = SettingsForm(request.POST)
        email = form.data['email']
    else:
        form = SettingsForm()
        state = 'no'

    return render_to_response('user_settings.html', {
        'state' : state,
        'username' : username,
        'form' : form,
        }, context_instance=RequestContext(request))
