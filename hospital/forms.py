from django import forms
from django.contrib.auth.models import User
from hospital.models import babyDetails

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password')

class babyDetailsForm(forms.ModelForm):

    class Meta:
        model = babyDetails
        fields = ('body_color','sex','delivery_time','hospital_name','blood_group','weight','handicap','aids','doctor_name','case_type')
