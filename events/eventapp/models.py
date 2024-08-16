from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Event(models.Model):

    title=models.CharField(max_length=50)
    picture=models.ImageField(upload_to='pic')
    venue=models.CharField(max_length=200,default='Venue ')
    location=models.CharField(max_length=200,default='Location currently unavailable')
    
    eve_date=models.DateField()
    desc=models.TextField()
    def __str__(self):
        return self.title
    
class Booking(models.Model):
    cus_name=models.CharField(max_length=50)
    phone=models.CharField( max_length=10)
    eve=models.ForeignKey(Event,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cus_name

class ContactUs(models.Model):
    name=models.CharField(max_length=50)
    e_mail=models.EmailField(max_length=50)
    message_us=models.TextField()

    def __str__(self):
        return self.name
    