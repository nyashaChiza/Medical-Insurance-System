from django.urls import path
from . import views
from dashboard.views import DashboardListView

urlpatterns = [
    path('dashboard', DashboardListView.as_view(), name="dashboard"),   
]
