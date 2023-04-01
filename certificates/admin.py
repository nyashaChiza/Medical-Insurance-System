from django.contrib import admin

from .models import Certificate, CertificateValidation

# Register your models here.

admin.site.register(Certificate)
admin.site.register(CertificateValidation)
