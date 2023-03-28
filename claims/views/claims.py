from django.shortcuts import render
from django.views.generic import  CreateView, DeleteView, DetailView, ListView, UpdateView
from claims.models import Claim
from claims.forms import ClaimsForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.http import HttpResponse
import xlwt
import pandas as pd
from io import BytesIO

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

def download_claims(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="claims.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Claims')

    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Patient Name', 'Location', 'Gender', 'Email','Cause', 'Employer', 'Relationship', 'Patient Suffix', 'NOD', 'Fee Charged', 'Service Provider' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) 

    font_style = xlwt.XFStyle()
    rows = Claim.objects.all().values_list('patience_name', 'location', 'gender','email','cause','employer','relationship','patient_suffix','number_of_dependants','fee_charged', 'service_provider')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
    
