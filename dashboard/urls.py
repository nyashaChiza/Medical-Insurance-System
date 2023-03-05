from django.urls import path
from . import views
from dashboard.views import DashboardListView

urlpatterns = [
    path('', DashboardListView.as_view(), name="dashboard"),   
]
