from django import forms
from .models import UserInfo



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