from django import forms
from django.forms import ModelForm
from claims.models import Claim


class ClaimsForm(ModelForm):
    
    class Meta:
        model = Claim
        fields = '__all__'
        