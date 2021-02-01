from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=255, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
