from django.shortcuts import render
from django.views.generic import  CreateView, DeleteView, DetailView, ListView, UpdateView
from claims.models import Claim
from claims.forms import ClaimsForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.conf import settings
import random
from claims.helpers import Classification

class ClaimsListView(ListView):
    model = Claim
    context_object_name = 'claim'
    template_name = 'claims/index.html'
    
class ClaimsCreateView(SuccessMessageMixin, CreateView):
    model = Claim
    form_class = ClaimsForm
    template_name = 'claims/create.html'
    success_message = "Claim created successfully"
    
    def form_valid(self, form):
        gender = 'male' if form.instance.gender else 'female'
        
        for cause in settings.CAUSE_CHOICES:
            if cause[0] == form.instance.cause:
                selected_cause = cause[1]

        data ={'member-name': 'Evans', 'gender': gender, 'email': 'raskawrq@washington.edu', 'location': 'Gweru', 'employer': 'Mudo', 'relationship': form.instance.relationship, 'patient_name': 'Samvura', 'patient_suffix':random.randint(100,999)  , 'patient_dob': '09/10/1986', 'number_of_dependants': form.instance.number_of_dependents, 'Fee Charged': form.instance.fee_charged, 'cause': selected_cause, 'number_of_claims': random.randint(0,6) , 'membership_period': random.randint(0,15) }
        classifier = Classification(data)
        classification = classifier.classify()
        
        form.instance.classification = 'Clean' if classification else 'Fraud'
        form.save()
        
        settings.LOGGER.debug(f"classification: {classification}")
        
        return super().form_valid(form)
    
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
