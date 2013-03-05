from django import forms
from ajax_select.fields import AutoCompleteSelectField

class FermentableForm(forms.Form):
	amount = forms.DecimalField(label="Amount (lbs)",
		 max_digits=4, decimal_places=2)
	name = forms.CharField(label="Ingredient", max_length=45)
	potential_extract = forms.DecimalField(label="PPG",
			    max_digits=5, decimal_places=4)
	color = forms.IntegerField(label="Color (L)")
	use = forms.CharField(label="Use", max_length=128)

class HopForm(forms.Form):
	time = forms.IntegerField(label="Time") # in minutes
	amount = forms.DecimalField(label="Amount (oz)",
		 max_digits=4, decimal_places=2)
	use = forms.CharField(label="Use", max_length=128)
	name = AutoCompleteSelectField("Hop Variety",
		required=False, help_text=None,
		plugin_options = {'autoFocus':True,'minLength':4})
	alpha_acid = forms.DecimalField("Alpha Acid",
		     max_digits=3, decimal_places=1)

class YeastForm(forms.Form):
	name = forms.CharField(label="Yeast",
		max_length=128)
	description = forms.CharField(label="Description",
		max_length=128)
	flocullation = forms.CharField(label="Flocculation",
		max_length=128)
	attenuation = forms.IntegerField(label="Attenuation")

class MiscForm(forms.Form):
	name = forms.CharField(label="Ingredient", max_length=128)
	description = forms.CharField(label="Description",
		max_length=128)
	time = forms.IntegerField(label="Time") # in minutes
	amount = forms.DecimalField(label="Amount (oz)",
		 max_digits=6, decimal_places=2)
	use = forms.CharField(label="Use", max_length=128)
	
class CommentForm(forms.Form):
	text = forms.CharField(label="Comment", max_length=1024)
