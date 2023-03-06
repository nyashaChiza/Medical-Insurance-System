
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

GENDER = settings.GENDER_CHOICES
RELATIONSHIP = settings.RELATIONSHIP

class Claim(models.Model):
    patience_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices= GENDER)
    date_of_birth = models.DateTimeField()
    email = models.EmailField(unique  = True)
    cause = models.CharField(max_length=255)
    employer = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255, choices= RELATIONSHIP)
    patient_suffix = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255)
    number_of_dependants = models.CharField(max_length=255)
    fee_charged = models.CharField(max_length=255)
    service_provider = models.ForeignKey('service_providers.ServiceProvider', on_delete=models.RESTRICT)
    
    
    def __str__(self):
        return self.patience_name
