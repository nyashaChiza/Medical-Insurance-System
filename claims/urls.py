from django.urls import path
from claims import views

from .views import(
    
    # Urls for claims
    ClaimsListView,
    ClaimsCreateView,
    ClaimsUpdateView,
    ClaimsDeleteView,
    ClaimsDetailView,
    download_claims
)

urlpatterns = [
    path('claims-index', ClaimsListView.as_view(),name = "claims-index"),
    path('create-claim', ClaimsCreateView.as_view(),name = "create-claim"),
    path('update-claim/<int:pk>/', ClaimsUpdateView.as_view(), name="update-claim"),
    path('delete-claim/<int:pk>/', ClaimsDeleteView.as_view(), name="delete-claim"),
    path('claim-details/<int:pk>/', ClaimsDetailView.as_view(), name="claim-details"),
    path('download-claims/', views.download_claims, name="download-claims"),

]
