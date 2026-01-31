from django import forms
from .models import MeetingRequest

class MeetingRequestForm(forms.ModelForm):
    
    class Meta:
        model = MeetingRequest
        fields = ['name', 'meeting_time', 'service', 'new_client', 'comment']
        
        widgets = {
            'meeting_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Please describe the reason for your meeting request...'}),
        }
        labels = {
            'meeting_time': 'Date and Time',
            'new_client': 'Are you a new client?',
        }