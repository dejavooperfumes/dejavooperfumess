from django import forms
from .models import Order
from django.contrib.auth.models import User


class OrderCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        self.fields['userid']= forms.ModelChoiceField(label="user", widget=forms.HiddenInput(attrs={'value':user}),
        queryset=User.objects.all())
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'phone', 'postal_code', 'city','userid']

