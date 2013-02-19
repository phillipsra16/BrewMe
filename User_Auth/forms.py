from django import forms
import re
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=32)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(
            label='Password',
            widget=forms.PasswordInput()
            )
    password2 = forms.CharField(
            label='Confirm Password',
            widget=forms.PasswordInput()
            )

    def clean_username(self):
        username = self.data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Username can only contain alphanumeric \
                    characters and the underscore')
        try:
            User.objects.get(username=username)

        except ObjectDoesNotExist:
            return username

        raise forms.ValidationError('Username is already taken.')
