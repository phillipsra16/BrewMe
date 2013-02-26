from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    state = username = ''
    #Do some fun things
    if state == '':
        state = 'Welcome!'
        uid = request.session['user_id']
        username = User.objects.get(id = uid)

    return render_to_response('home.html', {
        'state' : state,
        'username' : username,
        }, context_instance=RequestContext(request))
