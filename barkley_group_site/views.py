from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import MeetingRequestForm


# Create your views here.

def home(request):
    return render(request, "home.html")

def our_services(request):
    return render(request, "our_services.html")

def request_meeting(request):
    return render(request, "request_meeting.html")

def request_meeting(request):
    if request.method == 'POST':
        form = MeetingRequestForm(request.POST)
        if form.is_valid():
            meeting_request = form.save() 
            
            subject = f"New Meeting Request: {meeting_request.service} - {meeting_request.name}"
            message = (
                f"Name: {meeting_request.name}\n"
                f"Service: {meeting_request.service}\n"
                f"Date: {meeting_request.meeting_time}\n"
                f"Comment:\n{meeting_request.comment}"
            )
            
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['declan.watts97@gmail.com'],
                fail_silently=False,
            )
            
            return redirect('meeting_request_success')
    else:
        
        form = MeetingRequestForm()

    return render(request, "request_meeting.html", {"form": form})

def meeting_request_success(request):
    return render(request, "meeting_request_success.html")

