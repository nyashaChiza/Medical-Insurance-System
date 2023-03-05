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


class CertificateValidationCreateView(CreateView, SuccessMessageMixin):
    model = CertificateValidation
    form_class = CreateCertficateValidationForm
    template_name = "validation/create.html"
    success_message = "Certificate Submitted Successfully"
    
    def get_success_url(self):
        return reverse('certificates-index')
    
    