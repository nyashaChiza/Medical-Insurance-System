from django.db import models

STATUS_OPTIONS = (('Fake', 'Fake'), ('Clean', 'Clean'))

class CertificateValidation(models.Model):
    status =  models.CharField(max_length=30, choices=STATUS_OPTIONS, null=True, blank=True)
    title = models.CharField(max_length=300, null=True)
    certificate = models.FileField(upload_to='uploade_certificates/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
