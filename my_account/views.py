from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Service
from .forms import ServiceForm

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

@login_required
def checkout_view(request):
    return render(request, 'checkout.html')