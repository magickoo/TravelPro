from django import forms  
from .models import Client,Car

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        
class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'