from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    profile_pic = models.ImageField(upload_to='u_pics/')
