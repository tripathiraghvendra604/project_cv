from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    dob = models.DateField(auto_now_add=False, auto_now=False)
    place_of_birth = models.CharField(max_length=100)
    image = models.ImageField(null=False,
                              blank=False,
                              width_field='width_field',
                              height_field='height_field'
                              )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
