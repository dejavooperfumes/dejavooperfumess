from django import forms
from perfumes.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class feedbackform(forms.ModelForm):
    class Meta:
        model=feedback
        fields='__all__'
class SignForm(UserCreationForm):
    class Meta:
        model=User
        fields=('first_name','last_name','username','email','password1','password2',)
class reviewform(forms.ModelForm):
    class Meta:
        model=review
        fields='__all__' 