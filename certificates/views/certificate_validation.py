from django.shortcuts import render, reverse
from certificates.models import CertificateValidation
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
)
from django.contrib.messages.views import SuccessMessageMixin
from certificates.forms import CreateCertficateValidationForm
from django.conf import settings

class CertificateValidationCreateView(CreateView, SuccessMessageMixin):
    model = CertificateValidation
    form_class = CreateCertficateValidationForm
    template_name = "validation/create.html"
    success_message = "Certificate Submitted Successfully"
    
    def get_success_url(self):
        return reverse('validation-index')
    

class CertificateValidationListView(ListView, SuccessMessageMixin):
    model = CertificateValidation
    context_object_name= 'certificates'
    template_name= 'validation/index.html'
    
    
class CertificateValidationDeleteView(SuccessMessageMixin, DeleteView):
    model = CertificateValidation
    success_message = "Certificate Validation Deleted Successfully"
    
    def get_success_url(self):
        return reverse("validation-index")
    
    
    