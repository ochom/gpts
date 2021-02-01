from django.db import models


# Create your models here.
class MailList(models.Model):
    email = models.EmailField(max_length=255, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
