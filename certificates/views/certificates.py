from django.shortcuts import render, reverse
from certificates.models import Certificate
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
)
from django.contrib.messages.views import SuccessMessageMixin
from certificates.forms import CreateCertficateForm, UpdateCertficateForm


class CertificateCreateView(CreateView, SuccessMessageMixin):
    model = Certificate
    form_class = CreateCertficateForm
    template_name = "certificates/create.html"
    success_message = "Certificate Created Successfully"
    
    def get_success_url(self):
        return reverse('certifcate-index')

class CertificateListView(ListView):
    model = Certificate
    context_object_name = "certificates"
    template_name = "certificates/index.html"
    
class CertificateDetailView(DetailView):
    model = Certificate
    context_object_name = "certificate"
    template_name = "certificates/detail.html"
    
    
class CertificateUpdateView(UpdateView, SuccessMessageMixin):
    model = Certificate
    form_class = UpdateCertficateForm
    context_object_name = "certificate"
    template_name = "certificates/update.html"
    success_message = "Certificate Updated Successfully"
    
    def get_success_url(self):
        return reverse('certifcate-index')