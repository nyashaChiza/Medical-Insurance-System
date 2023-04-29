from logging import info
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from certificates.models import CertificateValidation
from claims.models import Claim
from certificates.helpers import send_reminders

class DashboardListView(TemplateView):
    
    template_name = 'dashboard/dashboard.html'
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['clean_certificates'] = CertificateValidation.objects.filter(status = 'Clean').count()
        context['fake_certificates'] = CertificateValidation.objects.filter(status = 'Fake').count()
        context['clean_claims'] = Claim.objects.filter(classification = 'Clean').count()
        context['fraud_claims'] = Claim.objects.filter(classification = 'Fraud').count()  

        return context      
        
