from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from .views import CertificateListView, CertificateDetailView,CertificateUpdateView, CertificateCreateView, CertificateValidationCreateView, CertificateDeleteView

urlpatterns = [
    path("index/", CertificateListView.as_view(), name="certificates-index"),
    path("create/", CertificateCreateView.as_view(), name="certificate-create"),
    path("details/<int:pk>", CertificateDetailView.as_view(), name="certificate-detail"),
    path("update/<int:pk>", CertificateUpdateView.as_view(), name="update-certificate"),
    path("delete/<int:pk>", CertificateDeleteView.as_view(), name="delete-certificate"),
    
    #Validation URLs
    path("validation/create/", CertificateValidationCreateView.as_view(), name="validation-create"),
]