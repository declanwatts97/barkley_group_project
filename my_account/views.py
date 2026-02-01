from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Service
from .forms import ServiceForm
import stripe

def my_account(request):
    return render(request, "my_account.html")

@login_required
def my_account_view(request):
    services = Service.objects.filter(user=request.user)
    
    if request.method == 'POST':
        if 'add_service' in request.POST:
            form = ServiceForm(request.POST)
            if form.is_valid():
                service = form.save(commit=False)
                service.user = request.user
                service.save()
                return redirect('my_account') # Use the name from your urls.py
        
        elif 'delete_service' in request.POST:
            service_id = request.POST.get('service_id')
            service = get_object_or_404(Service, id=service_id, user=request.user)
            service.delete()
            return redirect('my_account')
    
    else:
        form = ServiceForm()

    return render(request, 'my_account.html', {
        'services': services,
        'form': form
    })

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout_view(request):
    intent = stripe.PaymentIntent.create(
        amount=15000,
        currency='gbp',
    )
    return render(request, 'checkout.html', {
        'client_secret': intent.client_secret,
        'publishable_key': settings.STRIPE_PUBLISHABLE_KEY 
    })


@login_required
def payment_success_view(request):
    payment_intent_id = request.GET.get('payment_intent', '')
    return render(request, 'payment_success.html', {
        'payment_intent_id': payment_intent_id
    })