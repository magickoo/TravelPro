from django import forms  
from .models import Car, Booking

#class ClientForm(forms.ModelForm):
 #   class Meta:
   #     model = Client
    #    fields = '__all__'
        
class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['car', 'pickup_location', 'dropoff_location']  