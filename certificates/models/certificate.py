from django.db import models
import uuid

from service_providers.models import ServiceProvider

class Certificate(models.Model):
    title = models.CharField(max_length=255)
    issuer = models.CharField(max_length=30)
    path = models.TextField(null=True, blank=True)
    validity_period_in_months = models.IntegerField()
    hash = models.TextField(default=uuid.uuid4())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    service_provider = models.OneToOneField(ServiceProvider, related_name='my_certificate', on_delete=models.SET_NULL, null=True, blank=True)
    #toDo: add serviceprovider reverse
    
    def __str__(self):
        return self.title