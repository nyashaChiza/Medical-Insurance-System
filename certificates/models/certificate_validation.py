from django.db import models

STATUS_OTIONS = (('Fraud', 'Fraud'), ('Clean', 'Clean'))

class CertificateValidation(models.Model):
    status =  models.CharField(max_length=30, choices=STATUS_OTIONS, null=True, blank=True)
    title = models.CharField(max_length=300, null=True)
    certificate = models.FileField(upload_to='uploade_certificates/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.certificate} - {self.status}"
