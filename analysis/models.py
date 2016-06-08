from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    image = models.ImageField
