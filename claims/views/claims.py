from django.shortcuts import render
from django.views.generic import  CreateView, DeleteView, DetailView, ListView, UpdateView
from claims.models import Claim
from claims.forms import ClaimsForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse

class ClaimsListView(ListView):
    model = Claim
    context_object_name = 'claim'
    template_name = 'claims/index.html'
    
class ClaimsCreateView(SuccessMessageMixin, CreateView):
    model = Claim
    form_class = ClaimsForm
    template_name = 'claims/create.html'
    success_message = "Claim created successfully"
    
    def get_success_url(self):
        return reverse("claims-index")

class ClaimsUpdateView(SuccessMessageMixin, UpdateView):
    model = Claim
    context_object_name = 'claim'
    template_name = 'claims/update.html'
    form_class = ClaimsForm
    success_message = "Claim updated successfully"
    
    def get_success_url(self):
        return reverse("claims-index")

class ClaimsDeleteView(SuccessMessageMixin, DeleteView):
    model = Claim
    #TODO: success message not displaying
    success_message = "Claim deleted successfully"
    
    def get_success_url(self):
        return reverse("claims-index")

class ClaimsDetailView(DetailView):
    model = Claim
    context_object_name = "claim"
    template_name = "claims/detail.html"
