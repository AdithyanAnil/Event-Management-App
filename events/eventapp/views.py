from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from.models import Event,ContactUs
from.forms import BookingForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'index.html')
def create(request):
    if request.POST:
        title=(request.POST.get('title'))
        picture=(request.POST.get('picture'))
        eve_date=(request.POST.get('date'))
        desc=(request.POST.get("desc"))
        info=Event(title=title,picture=picture,eve_date=eve_date,desc=desc)
        info.save()
    return render(request,'create.html')
def list(request):
    list=Event.objects.all()
    print(list)
    return render(request,'list.html',{'events':list})
def home(request):
    return render(request,'home.html')
# @login_required(login_url='login/')
def booking(request):
    # if request.POST:
    form=BookingForm()
    dict_form={
    'form':form
        }
    return render(request,'booking.html',{'form':form})
def contact(request):
    if request.POST:
        name=(request.POST.get('name'))
        e_mail=(request.POST.get('e_mail'))
        message_us=(request.POST.get('message_us'))
        infom=ContactUs(name=name,e_mail=e_mail,message_us=message_us)
        infom.save()
    return render(request,'contact.html')