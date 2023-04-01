from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from .views import CertificateListView,CertificateValidationListView, CertificateValidationDeleteView, CertificateDetailView, CertificateUpdateView, CertificateCreateView, CertificateValidationCreateView, CertificateDeleteView, CertificateDownloadView

urlpatterns = [
    path("index/", CertificateListView.as_view(), name="certificates-index"),
    path("create/", CertificateCreateView.as_view(), name="certificate-create"),
    path("details/<int:pk>", CertificateDetailView.as_view(),
         name="certificate-detail"),
    path("update/<int:pk>", CertificateUpdateView.as_view(),
         name="update-certificate"),
    path("delete/<int:pk>", CertificateDeleteView.as_view(),
         name="delete-certificate"),
    path("certificate/download/<int:certificate_id>/",
         CertificateDownloadView.as_view(), name="download-certificate"),

    # Validation URLs
    path("validation/index/", CertificateValidationListView.as_view(),
         name="validation-index"),
    path("validation/create/", CertificateValidationCreateView.as_view(),
         name="validation-create"),
    path("validation/delete/<int:pk>", CertificateValidationDeleteView.as_view(),
         name="delete-certificate-validation"),
]
