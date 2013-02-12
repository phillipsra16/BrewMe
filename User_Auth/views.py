# User_Authentication views
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login

# User login view
def user_login(request):
    state = 'Please log in below'
    # Instantiate these variables to null
    username = password = ''
    # If the request is type 'POST'
    if request.POST:
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

    # Send back a response
    return render_to_response('auth.html', {
        'state' : state,
        'username' : username,
        })
