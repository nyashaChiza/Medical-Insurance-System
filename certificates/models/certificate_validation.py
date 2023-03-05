from django.db import models

STATUS_OTIONS = (('Fraud', 'Fraud'), ('Clean', 'Clean'))

class CertificateValidation(models.Model):
    status =  models.CharField(max_length=30)
    certificate = models.OneToOneField('certificates.Certificate',on_delete=models.SET_NULL, related_name='validation')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.certificate} - {self.status}"
