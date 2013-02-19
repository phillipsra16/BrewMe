# User_Authentication views
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django import forms
from User_Auth.forms import *
from django.template import RequestContext
from django.http import HttpResponseRedirect

# User login view
def user_login(request):
    if request.user.is_authenticated():
        u = 1
        #Do something, probably redirect

    else:
        state = 'Please log in below'
        # Instantiate these variables to null
        username = password = ''
        # If the request is type 'POST'
        if request.method == 'POST':
            # Set Username and pass
            username = request.POST.get('username')
            password = request.POST.get('password')
            # Use django's built in authentication method
            user = authenticate(username=username, password=password)

            # Handle the various cases
            if user is not None:
                if user.is_active:
                    login(request, user)
                    state = "You're successfully logged in!"
                else:
                    state = "Your account is not active"

            else:
                state = "Username and/or Password incorrect"

        #If the request is type 'GET'
        if request.method == 'GET':
            state = 'Create a User'
            return render_to_response('user_create.html', {
                'state' : state,
                })

        # Send back a response
        return render_to_response('auth.html', {
            'state' : state,
            'username' : username,
            })

def user_create(request):
    #Do something
    state = ''
    cont = True
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.data['password1'] == form.data['password2']:
            try:
                form.clean_username()
            except:
                cont = False
            if cont:
                user = User.objects.create_user(
                        username=form.data['username'],
                        password=form.data['password1'],
                        email=form.data['email']
                        )
                return HttpResponseRedirect('/login/')

        else:
            state = "Passwords don't match"

    else:
        state = 'Create an Account'
        form = RegistrationForm()

    return render_to_response('user_create.html', {
            'state' : state,
            'form' : form,
            }, context_instance=RequestContext(request))
