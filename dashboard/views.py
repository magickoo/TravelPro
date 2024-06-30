from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Booking, Client
from .forms import ClientForm

@login_required
def index(request):
    return render(request, 'dashboard/index.html')

@login_required
def staff(request):
    return render(request,'dashboard/staff.html')

@login_required
def clients(request):
    clients = Client.objects.all()
    
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-clients')
        
    else:
        form = ClientForm()
    context = {
        
       'clients': clients,
       'form': form,
        
    }
    return render(request,'dashboard/clients.html',context)

def clients_delete(request, pk):
    item = Client.objects.get(id = pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-clients')
    context = {
        'item': item
    }
    return render(request,'dashboard/clients_delete.html',context)

def clients_edit(request,pk):
    item = Client.objects.get(id=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST,instance = item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-clients')
        
    else:
        form = ClientForm(instance = item)
    
    context = {
        'form' : form,
    }
    
    return render(request, 'dashboard/clients_edit.html',context)

@login_required
def bookings(request):
    booking = Booking.objects.all()
    
    return render(request,'dashboard/bookings.html')