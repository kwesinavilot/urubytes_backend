from django.db import models
from django.contrib.auth.models import User

class Waitlist(models.Model):
    email = models.CharField(max_length=60)
    phoneNumber = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
    
class Contact(models.Model):
    email = models.CharField(max_length=60)
    phoneNumber = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email