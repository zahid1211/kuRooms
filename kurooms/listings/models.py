from django.db import models

class Property(models.Model):
    title = models.CharField(maxlength=100)
    description = models.TextField()
    address = models.CharField(maxlength=200)
    contact_1 = models.CharField(maxlength=10)
    contact_2 = models.CharField(maxlength=10)

    owner = models.ForeignKey(setting.AUTH_USER_MODEL, ondelete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 