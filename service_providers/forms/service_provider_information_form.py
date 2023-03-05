from django import forms
from django.forms import ModelForm
from service_providers.models import ServiceProvider


class ServiceProviderForm(ModelForm):
    
    class Meta:
        model = ServiceProvider
        exclude = ['created_at', 'updated_at']
        