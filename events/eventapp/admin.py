from django.contrib import admin
from.models import Booking,Event,ContactUs
# Register your models here.
admin.site.register(Event)
admin.site.register(Booking)
admin.site.register(ContactUs)