from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
CATEGORY = (
    ('Kia','Kia'),
    ('Suzuki Swift','Suzuki Swift'),
    ('Mahindra Scorpio','Mahindra Scorpio'),
    ('Hyundai','Hyundai'),
)
GENDER =(
    ('Male','Male'),
    ('Female','Female'),
    ('others','others'),
)

class Client(models.Model):
      name = models.CharField(max_length = 100, null=True)
      gender = models.CharField(max_length = 20,choices = GENDER, null = True)
      email = models.EmailField(max_length=100, unique=True, null= True)
      contact =  PhoneNumberField(null = True)
    
      def __str__(self):
        return f'{self.name}'
    
class Booking(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    car = models.CharField(max_length = 100,choices = CATEGORY, null = True)
    pickup_location = models.CharField(max_length=255, null= True)
    dropoff_location = models.CharField(max_length=255, null=False)
    pickup_date = models.DateTimeField(null=False)
    dropoff_date = models.DateTimeField(null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='pending')
    

    def __str__(self):
        return f"{self.client.name} - {self.car} ({self.pickup_date} to {self.dropoff_date})"
    