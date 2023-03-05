from django import forms
from django.forms import ModelForm
from service_providers.models import ServiceProvider


class ServiceProviderForm(ModelForm):
    
    class Meta:
        model = ServiceProvider
        fields = '__all__'
        