from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

def upload_location_img(instance, filename):
    return '%s/%s' %(instance.user, 'image')

def upload_location_dob_doc(instance, filename):
    return '%s/%s' %(instance.user, 'dob_doc')

class UserInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    dob = models.DateField(auto_now_add=False, auto_now=False)

    dob_doc = models.FileField(upload_to=upload_location_dob_doc,
                               null=True, blank=True)

    place_of_birth = models.CharField(max_length=100)

    image = models.ImageField(upload_to=upload_location_img,
                              null=False,
                              blank=False,
                              width_field='width_field',
                              height_field='height_field'
                              )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __str__(self):
        return self.fname


class EducationalInfo(models.Model):
    high_school = models.TextField()
    intermediate = models.TextField()
    graduation = models.FloatField()