from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Booking,  Car
from .forms import CarForm
from django.contrib.auth.models import User

@login_required
def index(request):
    return render(request, 'dashboard/index.html')

@login_required
def staff(request):
    workers = User.objects.all()
    context = {
        'workers' : workers
    }
    return render(request,'dashboard/staff.html',context)

@login_required
def staff_detail(request,pk):
    workers = User.objects.get(id = pk)
    context = {
        'workers' : workers
    }
    return render(request,'dashboard/staff_detail.html',context)

@login_required
def cars(request):
    cars = Car.objects.all()
    
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-cars')
        
    else:
        form = CarForm()
    context = {
        
       'cars': cars,
       'form': form,
        
    }
    return render(request,'dashboard/cars.html',context)

@login_required
def cars_delete(request, pk):
    item = Car.objects.get(id = pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-cars')
    context = {
        'item': item
    }
    return render(request,'dashboard/cars_delete.html',context)

@login_required
def cars_edit(request,pk):
    item = Car.objects.get(id=pk)
    if request.method == 'POST':
        form = CarForm(request.POST,instance = item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-cars')
        
    else:
        form = CarForm(instance = item)
    
    context = {
        'form' : form,
    }
    
    return render(request, 'dashboard/cars_edit.html',context)


@login_required
def bookings(request):
    booking = Booking.objects.all()
    context = {
        'booking' : booking,
    }
    return render(request,'dashboard/bookings.html',context)