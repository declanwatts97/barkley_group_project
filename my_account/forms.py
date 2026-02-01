from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service_type', 'is_active']
        labels = {
            'service_type': 'Service Type',
            'is_active': 'Active Status'
        }