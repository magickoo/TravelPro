from django.contrib import admin
from .models import Client, Booking, Car
from django.contrib.auth.models import Group

admin.site.site_header = 'RR Travels Dashboard'

#class ProductAdmin(admin.ModelAdmin):
 #   list_display = ('name','car')
  #  list_filter = ['car']
    
    
admin.site.register(Client)
admin.site.register(Booking)
admin.site.register(Car)