from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Booking,  Car
from .forms import CarForm, BookingForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Count
import json
from django.db.models.functions import TruncDate

@login_required
def index(request):
    booking = Booking.objects.all()
    booking_count = booking.count()
    car = Car.objects.all()
    #car_booking_counts = Booking.objects.values('car__name').annotate(count=models.Count('car__name'))
    car_counts = Car.objects.values('type').annotate(count=Count('name'))
    car_count = car.count()
    customer = User.objects.all()
    customer_count = customer.count()
    
    #booking_counts = Booking.objects.values('date').annotate(count=Count('id'))
    booking_by_date = booking.annotate(trunc_date=TruncDate('date')).values('trunc_date').annotate(count=Count('id')).order_by('trunc_date')
   

    # Prepare data for chart
    labels = []
    data = []
    #for booking in booking_counts:
     #   labels.append(booking['date'].strftime('%Y-%m-%d'))  # Format date as needed
      #  data.append(booking['count'])

    # Convert data to JSON format for JavaScript
    labels_json = json.dumps(labels)
    data_json = json.dumps(data)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.client = request.user  # Set the client to the current user
            obj.save()
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
        'labels_json': labels_json,
        'data_json': data_json,
        'booking_by_date' : booking_by_date,
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
def booking(request):
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