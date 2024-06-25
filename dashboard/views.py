from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Booking

@login_required
def index(request):
    return render(request, 'dashboard/index.html')

@login_required
def staff(request):
    return render(request,'dashboard/staff.html')

@login_required
def clients(request):
    return render(request,'dashboard/clients.html')

@login_required
def bookings(request):
    booking = Booking.objects.all()
    
    return render(request,'dashboard/bookings.html')