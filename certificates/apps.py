from django.apps import AppConfig


class CertificatesConfig(AppConfig):
    
    def ready(self):
        from certificates.signals import generate_certificate, validate_certificate
        return super().ready()
    
    default_auto_field = "django.db.models.BigAutoField"
    name = "certificates"
