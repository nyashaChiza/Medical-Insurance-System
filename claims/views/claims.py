from django.shortcuts import render
from django.views.generic import  CreateView, DeleteView, DetailView, ListView, UpdateView
from claims.models import Claim
from claims.forms import ClaimsForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.http import HttpResponse
import xlwt
import pandas as pd
from django.conf import settings


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

def download_claims(request):
    import random
    title = f"claims-report-{random.randint(1000,9999)}.xls"
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename="{title}"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Claims')

    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Patient Name', 'Location', 'Gender', 'Email','Cause', 'Employer', 'Relationship', 'Patient Suffix', 'NOD', 'Fee Charged', 'Classification Status' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) 

    font_style = xlwt.XFStyle()
    rows = Claim.objects.all().values_list('patience_name', 'city', 'gender','email','cause','employer','relationship','patient_suffix','number_of_dependents','fee_charged', 'classification')
    for row in rows:
        settings.LOGGER.critical(row)
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
    
