from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('create/',views.create,name='create'),
    path('events/',views.list,name='list'),
    path('booking/',views.booking,name='booking'),
    path('contact/',views.contact,name='contact'),
    
]