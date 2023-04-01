from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from certificates.models import Certificate, CertificateValidation
from certificates.helpers import validate
import random

@receiver(post_save, sender=CertificateValidation, dispatch_uid='validate_certificate')
def validate_certificate(sender, instance, created, **kwargs):
    if created:
        settings.LOGGER.critical(instance.certificate)
        status = random.choice(['Clean', 'Fake'])
        certificate = Certificate.objects.first()
        
        if certificate:
            instance.status = status
            instance.save()
            settings.LOGGER.success(f'{instance.title} generated successfully')
        else:
            instance.status = status
            instance.save()
            settings.LOGGER.error(f'{instance.title} certificate generation failed')
        