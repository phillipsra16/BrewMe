from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class Style(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    ibu_max = models.IntegerField()
    ibu_min = models.IntegerField()
    original_gravity = models.IntegerField()
    final_gravity = models.IntegerField()
    color = models.IntegerField()

class Recipe(models.Model):
    name = models.CharField(max_length=128)
    user_id = models.ForeignKey(User)
    yeast_id = models.CharField(max_length=64)
    parent_id = models.ForeignKey('self',
                                  blank=True,
                                  null=True)
    style_id = models.ForeignKey(Style)
    description = models.CharField(max_length=1024)

    def __unicode__(self):
        return self.name

class Fermentable(models.Model):
    name = models.CharField(max_length=128)
    color = models.CharField(max_length=8)
    potential_extract = models.DecimalField(max_digits=6,
                                            decimal_places=3)
    use = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

class Hop(models.Model):
    name = models.CharField(max_length=128)
    alpha_acid = models.DecimalField(max_digits=6,
                                     decimal_places=3)
    description = models.CharField(max_length=128)
    use = models.IntegerField()

    def __unicode__(self):
        return self.name

class Yeast(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    flocculation = models.DecimalField(max_digits=6,
                                       decimal_places=3)
    attenuation = models.DecimalField(max_digits=6,
                                      decimal_places=3)

    def __unicode__(self):
        return self.name

class Misc(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

class Comments(models.Model):
    user_id = models.ForeignKey(User)
    recipe_id = models.ForeignKey(Recipe)
    active = models.BooleanField()
    text = models.CharField(max_length=1024)

class GrainBill(models.Model):
    recipe_id = models.ForeignKey(Recipe)
    fermentable_id = models.ForeignKey(Fermentable)
    amount = models.DecimalField(max_digits=8,
                                 decimal_places=2)
    use = models.IntegerField()

class HopSchedule(models.Model):
    recipe_id = models.ForeignKey(Recipe)
    hop_id = models.ForeignKey(Hop)
    time = models.TimeField()
    amount = models.DecimalField(max_digits=8,
                                  decimal_places=2)
    use = models.IntegerField()

class MiscBill(models.Model):
    recipe_id = models.ForeignKey(Recipe)
    misc_id = models.ForeignKey(Misc)
    time = models.TimeField()
    amount = models.DecimalField(max_digits=8,
                                  decimal_places=2)
    use = models.IntegerField()

    def __unicode__(self):
        return self.name
