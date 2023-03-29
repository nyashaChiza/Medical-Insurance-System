from django import forms
from django.forms import ModelForm
from claims.models import Claim


class ClaimsForm(ModelForm):
    
    class Meta:
        model = Claim
        exclude = ['classification']
        widgets = {'date_of_birth': forms.TextInput(attrs={'type': 'date'})}
        