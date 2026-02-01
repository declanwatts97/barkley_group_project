from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    SERVICE_CHOICES = [
        ('personal_tax', 'Personal Tax'),
        ('corp_tax', 'Corporation Tax'),
        ('payroll', 'Payroll'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_services")
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    is_active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_service_type_display()}"