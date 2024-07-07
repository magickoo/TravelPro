from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Booking,  Car
from .forms import CarForm, BookingForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Count

@login_required
def index(request):
    booking = Booking.objects.all()
    booking_count = booking.count()
    car = Car.objects.all()
    #car_booking_counts = Booking.objects.values('car__name').annotate(count=models.Count('car__name'))
    car_counts = Car.objects.values('name').annotate(count=Count('name'))
    car_count = car.count()
    customer = User.objects.all()
    customer_count = customer.count()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer = request.user
            obj.save()
            form.save()
            return redirect('dashboard')
    else:
        form = BookingForm()
    context = {
        'booking' : booking,
        'form' : form,
        'car' : car,
        'booking_count' : booking_count,
        'car_count' : car_count,
        'customer_count' : customer_count,
        'car_counts' : car_counts,
        #'car_booking_counts': car_booking_counts,,
    }
    return render(request, 'dashboard/index.html',context)

@login_required
def staff(request):
    workers = User.objects.all()
    car = Car.objects.all()
    car_count = car.count()
    booking = Booking.objects.all()
    booking_count = booking.count()
    customer = User.objects.all()
    customer_count = customer.count()
    context = {
        'workers' : workers, 
        'car_count' : car_count,
        'customer_count' : customer_count,
        'booking_count' : booking_count
        
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
    car = Car.objects.all()
    car_count = car.count()
    booking = Booking.objects.all()
    booking_count = booking.count()
    customer = User.objects.all()
    customer_count = customer.count()
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-cars')
        
    else:
        form = CarForm()
    context = {
    'car_count': car_count,
    'booking_count' : booking_count,
    'customer_count' : customer_count,
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
    booking_count = booking.count()
    customer = User.objects.all()
    customer_count = customer.count()
    car = Car.objects.all()
    car_count = car.count()
    
    
    context = {
        'booking' : booking,
        'booking_count' : booking_count,
        'customer_count' : customer_count,
        'car_count': car_count
    }
    return render(request,'dashboard/bookings.html',context)