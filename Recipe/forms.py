from django import forms
from Recipe.models import Hop


class FermentableForm(forms.Form):
    amount = forms.DecimalField(
            label="Amount (lbs)",
            max_digits=4,
            decimal_places=2)
    name = forms.CharField(
            label="Ingredient",
            max_length=45)
    potential_extract = forms.DecimalField(
            label="PPG",
            max_digits=5,
            decimal_places=4)
    color = forms.IntegerField(
            label="Color (L)")
    use = forms.CharField(
            label="Use",
            max_length=128)


class YeastForm(forms.Form):
    name = forms.CharField(
            label="Yeast",
            max_length=128)
    description = forms.CharField(
            label="Description",
            max_length=128)
    flocullation = forms.CharField(
            label="Flocculation",
            max_length=128)
    attenuation = forms.IntegerField(
            label="Attenuation")


class MiscForm(forms.Form):
    name = forms.CharField(
            label="Ingredient",
            max_length=128)
    description = forms.CharField(
            label="Description",
            max_length=128)
    time = forms.IntegerField(
            label="Time") # in minutes
    amount = forms.DecimalField(
            label="Amount (oz)",
            max_digits=6,
            decimal_places=2)
    use = forms.CharField(
            label="Use",
            max_length=128)


class CommentForm(forms.Form):
    text = forms.CharField(
            label="Comment",
            max_length=1024)


class HopForm(forms.Form):
    hop_name = forms.ModelChoiceField(
            label="Hop Variety",
            widget=forms.Select(attrs={'class':'selector'}),
            queryset=Hop.objects.all())
    time = forms.IntegerField(
            label="Time")
    amount = forms.DecimalField(
            label="Amount (oz)",
            max_digits=4,
            decimal_places=2)
    use = forms.CharField(
            label="Use",
            max_length=128)
    #name = forms.ModelChoiceField(label="Hop Variety",
            #queryset=Hop.objects.all(), class="selector")
    alpha_acid = forms.DecimalField(
            label="Alpha Acid",
            max_digits=3,
            decimal_places=1)

    def serialize_form(self):
        ser_form = {'hop_name' : str(self['hop_name']),
                    'time' : str(self['time']),
                    'amount' : str(self['amount']),
                    'use' : str(self['use']),
                    'alpha_acid' : str(self['alpha_acid']),}
        return ser_form

    """def __init__(self, *args, **kwargs):
        hop_name = kwargs.pop('hop_name','')
        super(HopForm, self).__init__(*args, **kwargs)
        if not hop_name:
            self.fields['alpha_acid'] = Hop.query.get(hop_name=hop_name).alpha_acid"""
