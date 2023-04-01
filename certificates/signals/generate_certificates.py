from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from certificates.models import Certificate
from certificates.helpers import CertificateGenerator
import random

@receiver(post_save, sender=Certificate, dispatch_uid='generate_certificate')
def generate_certificate(sender, instance, created, **kwargs):
    
    if created:
        certificate = CertificateGenerator(instance)
        
        if certificate.generate():
            settings.LOGGER.success(f'{instance.title} generated successfully')
        else:
             settings.LOGGER.error(f'{instance.title} certificate generation failed')
        