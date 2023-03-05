from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from certificates.views import CertificateListView, CertificateDetailView, CertificateCreateView

urlpatterns = [
    path("index/", CertificateListView.as_view(), name="certificates-index"),
    path("create/", CertificateCreateView.as_view(), name="certificate-create"),
    path("details/<int:pk>", CertificateDetailView.as_view(), name="certificate-detail"),
   
]