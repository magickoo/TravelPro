from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'dashboard/index.html')

def staff(request):
    return render(request,'dashboard/staff.html')

def clients(request):
    return render(request,'dashboard/clients.html')

def bookings(request):
    return render(request,'dashboard/bookings.html')