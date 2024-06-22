from django.contrib import admin
from .models import Client
from django.contrib.auth.models import Group

admin.site.site_header = 'RR Travels Dashboard'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','car')
    
    
admin.site.register(Client,ProductAdmin)