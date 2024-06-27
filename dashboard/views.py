from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Booking, Client

@login_required
def index(request):
    return render(request, 'dashboard/index.html')

@login_required
def staff(request):
    return render(request,'dashboard/staff.html')

@login_required
def clients(request):
    #client_count = client.count()
    #context = {
        
     #   'customer_count': customer_count,
        
    #}
    return render(request,'dashboard/clients.html')


@login_required
def bookings(request):
    booking = Booking.objects.all()
    
    return render(request,'dashboard/bookings.html')