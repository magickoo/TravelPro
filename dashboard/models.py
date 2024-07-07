from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

CATEGORY = (
    ('Kia','Kia'),
    ('Suzuki Swift','Suzuki Swift'),
    ('Mahindra Scorpio','Mahindra Scorpio'),
    ('Hyundai','Hyundai'),
    ('SUV','SUV'),
    ('Sedan','Sedan'),
    ('Tata','Tata'),
    ('Volvo','Volvo'),
    ('Bajaj','Bajaj'),
    ('Honda','Honda')
)
GENDER =(
    ('Male','Male'),
    ('Female','Female'),
    ('others','others'),
)
class Car(models.Model):
    name = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=20, choices=CATEGORY, null=True)
    rental_rate = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.name}'
    

    
class Booking(models.Model):
    client = models.ForeignKey(User,on_delete= models.CASCADE)
    car = models.ForeignKey(Car,on_delete= models.CASCADE)
    pickup_location = models.CharField(max_length=255, null= True)
    dropoff_location = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    date = models.DateTimeField(null = True)
    
    def __str__(self):
        return f'{self.client}'
    

    

    
    