import datetime
import os

from django.conf import settings
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from certificates.forms import CreateCertficateForm, UpdateCertficateForm
from certificates.helpers import (CertificateGenerator, add_months,
                                  send_reminder)
from certificates.models import Certificate


class CertificateCreateView(SuccessMessageMixin, CreateView):
    model = Certificate
    form_class = CreateCertficateForm
    template_name = "certificates/create.html"
    
        
    def get_success_url(self):
        return reverse('certificates-index')

class CertificateListView(ListView):
    model = Certificate
    context_object_name = "certificates"
    template_name = "certificates/index.html"
    
class CertificateDetailView(DetailView):
    model = Certificate
    context_object_name = "certificate"
    template_name = "certificates/detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['valid_until'] = add_months(context['certificate'].created, context['certificate'].validity_period_in_months)
        context['today'] = datetime.datetime.now()
        return context
    
class CertificateUpdateView(SuccessMessageMixin, UpdateView):
    model = Certificate
    form_class = UpdateCertficateForm
    context_object_name = "certificate"
    template_name = "certificates/update.html"
    success_message = "Certificate Updated Successfully"
    
    def get_success_url(self):
        return reverse('certificates-index')
    
    
class  CertificateDeleteView(SuccessMessageMixin, DeleteView):
    model = Certificate
    #TODO: success message not displaying
    success_message = "Certificate Deleted Successfully"
    
    def get_success_url(self):
        return reverse("certificates-index")
    
    
class CertificateDownloadView(TemplateView):
    def get(self, request, certificate_id, *args, **kwargs):
        certificate = Certificate.objects.get(pk=certificate_id)
        
        return self.download_report(certificate)
    
    def download_report(self, certificate: Certificate):
        with open( certificate.path, 'rb') as rf:
            response = HttpResponse(rf.read(), content_type="application/vnd.docx")
            response['Content-Disposition'] = f'inline; filename={os.path.basename(certificate.path)}'
            return response
        



class SendNotificationView(TemplateView):
    def get(self, request, certificate_id, *args, **kwargs):
        certificate = Certificate.objects.filter(id=certificate_id).first()  
        settings.LOGGER.success(send_reminder(certificate))
        messages.success(request,'Notification Sent Successfully')
        return redirect(reverse("certificates-index")) 