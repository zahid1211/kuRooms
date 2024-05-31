from django.db import models

# Create your models here.

class Owner(models.Model):
    name = models.CharField(max_length=100)
    phNumber = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
