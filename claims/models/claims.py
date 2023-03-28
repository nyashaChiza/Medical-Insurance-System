
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

GENDER_CHOICES = settings.GENDER_CHOICES
RELATIONSHIP_CHOICES = settings.RELATIONSHIP_CHOICES
CAUSE_CHOICES = settings.CAUSE_CHOICES
CLASS_CHOICES = settings.CLASS_CHOICES

class Claim(models.Model):
    patience_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    date_of_birth = models.DateTimeField()
    email = models.EmailField(unique=False)
    cause = models.CharField(max_length=255, choices=CAUSE_CHOICES)
    classification = models.CharField(max_length=20, choices=CLASS_CHOICES, default=None, null=True, blank=True)
    employer = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255, choices=RELATIONSHIP_CHOICES)
    patient_suffix = models.CharField(max_length=255)
    number_of_dependents = models.PositiveIntegerField(default=0)
    fee_charged = models.FloatField(default=0.00)
    service_provider = models.ForeignKey('service_providers.ServiceProvider', on_delete=models.RESTRICT)
    
    
    def __str__(self):
        return f"{self.patience_name} - {self.cause}"
