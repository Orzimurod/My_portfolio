from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13)
    theme = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
