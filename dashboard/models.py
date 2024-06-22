from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
CATEGORY = (
    ('Kia','Kia'),
    ('Suzuki Swift','Suzuki Swift'),
    ('Mahindra Scorpio','Mahindra Scorpio'),
    ('Hyundai','Hyundai'),
)

class Client(models.Model):
    name = models.CharField(max_length = 100, null=True)
    car = models.CharField(max_length = 100,choices = CATEGORY, null = True)
    destination = models.CharField(max_length = 100, null = True)
    contact =  PhoneNumberField(null = True)
    
    def __str__(self):
        return f'{self.name}'