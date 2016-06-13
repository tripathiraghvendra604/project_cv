from django import forms
from .models import UserInfo
from django.forms import formset_factory
from django.forms.formsets import BaseFormSet
from django.contrib import messages
from .models import PostGraduateCourse, UnderGraduateCourse



class DateInput(forms.DateInput):
    input_type = 'date'

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = [
            'fname',
            'lname',
            'dob',
            'place_of_birth',
            'image',
        ]
        widgets = {
            'dob': DateInput(),
        }

class EducationForm(forms.Form):
    '''highschool = forms.CharField(widget=forms.Textarea, max_length=500)
    intermediate = forms.CharField(widget=forms.Textarea, max_length=500)
    graduation = forms.CharField(widget=forms.Textarea, max_length=500)
    post_garduation = forms.CharField(widget=forms.Textarea, max_length=500)

'''

    # ug = UnderGraduateCourse.objects.all()
    # ug_choices = tuple([college.courses, college.courses] for college in ug)
    #
    # pg = PostGraduateCourse.objects.all()
    # pg_choices = tuple([college.courses, college.courses] for college in pg)

    ten_board = forms.CharField(max_length=100)
    ten_percent = forms.IntegerField(max_value=100)
    ten_file = forms.FileField()

    # Board12 = forms.CharField(max_length=100)
    # Percent12 = forms.IntegerField()
    File12 = forms.FileField()
    # Subject12 = forms.Textarea()
    # MarksScored12 = forms.Textarea()
    # MaximumMarks12 = forms.Textarea()
    # twelve_plus = forms.CharField(widget=forms.Textarea, max_length=500)
    # twelve_minus = forms.CharField(widget=forms.Textarea, max_length=500)

    g_board = forms.CharField(max_length=100)
    g_percent = forms.IntegerField(max_value=100)
    g_file = forms.FileField()

    pg_board = forms.CharField(max_length=100)
    pg_percent = forms.IntegerField(max_value=100)
    pg_file = forms.FileField()
