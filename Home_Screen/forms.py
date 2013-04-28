from django import forms
from Recipe.models import Recipe

class UserRecipeForm(forms.Form):
    name = forms.CharField(
            widget      = forms.Textarea,
            label       = "Name: ",
            max_length  = 128
    )
    style = forms.CharField(
            label       = "Style: ",
            max_length  = 64
    )
    id = forms.IntegerField(
            #widget      = forms.HiddenInput(),
    )
