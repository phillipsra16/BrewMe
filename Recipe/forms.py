from django import forms
from Recipe.models import Hop, Yeast, Fermentable


class FermentableForm(forms.Form):
    amount = forms.DecimalField(
            label="Amount (lbs)",
            max_digits=4,
            decimal_places=2)
    ferm_name = forms.ModelChoiceField(
            widget=forms.Select(attrs={'class':'selector'}),
            label="Ingredient",
            queryset=Fermentable.objects.all())
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
    yeast_name = forms.ModelChoiceField(
            widget=forms.Select(attrs={'class':'selector'}),
            label="Yeast",
            queryset=Yeast.objects.all())
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
            max_length=1024,
            widget=forms.Textarea())


class HopForm(forms.Form):
    hop_name = forms.ModelChoiceField(
            label="Hop Variety",
            widget=forms.Select(attrs={'class':'selector'}),
            queryset=Hop.objects.all())
    #the available times for hop additions
    TIME_CHOICES = (('90','90',),
                    ('80','80',),
                    ('70','70',),
                    ('60','60',),
                    ('55','55',),
                    ('50','50',),
                    ('45','45',),
                    ('40','40',),
                    ('35','35',),
                    ('30','30',),
                    ('25','25',),
                    ('20','20',),
                    ('15','15',),
                    ('10','10',),
                    ('5','5',),
                    ('0','0',))
    time = forms.IntegerField(
            label="Time",
            widget=forms.Select(choices = TIME_CHOICES))
    amount = forms.DecimalField(
            label="Amount (oz)",
            max_digits=4,
            decimal_places=2)
    # mask for hop usage
    HOP_USES = (('1','First Wort',),
                ('2','Boil',),
                ('3','Whirlpool',),
                ('4','Dry Hop',))
    use = forms.CharField(
            label="Use",
            widget=forms.Select(choices = HOP_USES),
            max_length=128)
    #name = forms.ModelChoiceField(label="Hop Variety",
            #queryset=Hop.objects.all(), class="selector")
    alpha_acid = forms.DecimalField(
            label="Alpha Acid",
            max_digits=3,
            decimal_places=1)

