import uuid

from dateutil.relativedelta import relativedelta
from django.db import models
from datetime import datetime
import pytz
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
    
    def valid_until(self):
        return self.created + relativedelta(months=self.validity_period_in_months)
    
    def get_status(self):
        utc=pytz.UTC
        return 'Valid' if utc.localize(datetime.now()) > self.valid_until() else 'Expired'