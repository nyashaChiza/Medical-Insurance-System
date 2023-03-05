from django.shortcuts import render
from django.views.generic import  CreateView, DeleteView, DetailView, ListView, UpdateView
from service_providers.models import ServiceProvider
from service_providers.forms import ServiceProviderForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse

class ServiceProviderListView(ListView):
    model = ServiceProvider
    template_name = 'service_provider/index.html'
    
class ServiceProviderCreateView(SuccessMessageMixin, CreateView):
    model = ServiceProvider
    form_class = ServiceProviderForm
    template_name = 'service_provider/create.html'
    success_message = "Service Provider created successfully"
    
    def get_success_url(self):
        return reverse("service-providers-index")

class ServiceProviderUpdateView(SuccessMessageMixin, UpdateView):
    model = ServiceProvider
    template_name = 'service_provider/update.html'
    form_class = ServiceProviderForm 
    success_message = "Service Provider updated successfully"
    
    def get_success_url(self):
        return reverse("service-providers-index")

class ServiceProviderDeleteView(SuccessMessageMixin, DeleteView):
    model = ServiceProvider
    #TODO: success message not displaying
    success_message = "Service Provider deleted successfully"
    
    def get_success_url(self):
        return reverse("service-providers-index")

class ServiceProviderDetailView(DetailView):
    model = ServiceProvider
    context_object_name = "service_provider"
    template_name = "service_provider/detail.html"
