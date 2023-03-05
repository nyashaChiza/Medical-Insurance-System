from django.db import models

class Certificate(models.Model):
    title = models.CharField(max_length=255)
    issuer = models.CharField(max_length=30)
    path = models.CharField(max_length=300)
    validity_period_in_months = models.IntegerField()
    hash = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #toDo: add serviceprovider reverse
    
    def __str__(self):
        return self.title