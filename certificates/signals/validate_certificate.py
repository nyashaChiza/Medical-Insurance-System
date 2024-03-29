from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from certificates.models import Certificate, CertificateValidation
from certificates.helpers import validate
import random
import os

@receiver(post_save, sender=CertificateValidation, dispatch_uid='validate_certificate')
def validate_certificate(sender, instance, created, **kwargs):
    if created:
        settings.LOGGER.critical(instance.certificate)

        path = os.path.join(settings.MEDIA_ROOT,instance.certificate.path )
        certificate = validate(path)
        if certificate:
            instance.status = 'Clean'
            instance.save()
            settings.LOGGER.success(f'{instance.title} generated successfully')
        else:
            instance.status = 'Fake'
            instance.save()
            settings.LOGGER.error(f'{instance.title} certificate generation failed')
        