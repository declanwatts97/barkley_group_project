from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db import models

class MeetingRequest(models.Model):
    SERVICE_CHOICES = [
        ('personal_tax', 'Personal Tax'),
        ('corp_tax', 'Corporation Tax'),
        ('payroll', 'Payroll'),
    ]

    NEW_CLIENT_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    name = models.CharField(max_length=100)
    meeting_time = models.DateTimeField()
    service = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    new_client = models.CharField(max_length=3, choices=NEW_CLIENT_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service}"