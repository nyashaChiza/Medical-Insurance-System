
from django.db import models
from django.contrib.auth import get_user_model


class ServiceProvider(models.Model):
    name = models.CharField(max_length=255)
    affoz_code = models.CharField(max_length=255, unique= True)
    website = models.URLField(max_length=255)
    contact = models.CharField(max_length=255)
    contact_personal_email = models.EmailField(unique  = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
