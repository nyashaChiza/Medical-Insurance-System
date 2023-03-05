from logging import info
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages

class DashboardListView(TemplateView):
    
    template_name = 'dashboard/dashboard.html'
