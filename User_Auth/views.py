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
    state = username = password = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password') + \
                'and boom goes the dynamite'
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

    if state == '':
        state = 'Please Log in'
        form = LoginForm()


    # Send back a response
    return render_to_response('user_login.html', {
        'state' : state,
        'username' : username,
        'form' : form
        }, context_instance=RequestContext(request))



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
                        password=form.data['password1'] + \
                        'and boom goes the dynamite',
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
