from django.shortcuts import render, redirect   

# Create your views here.

def home(request):
    return render(request, "home.html")

def our_services(request):
    return render(request, "our_services.html")

def request_meeting(request):
    return render(request, "request_meeting.html")

def my_account(request):
    return render(request, "my_account.html")

