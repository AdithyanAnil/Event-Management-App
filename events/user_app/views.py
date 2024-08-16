from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login as authlogin,logout as authlogout
from django.contrib import messages


def user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exist")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exist")
                return redirect('signup')
            else:
                user_reg=User.objects.create_user(username=username,email=email,password=password)
                user_reg.save()
                messages.info(request,"User created")
                return redirect('login')
        else:
            messages.info(request,"Password does'nt match")
            return redirect('signup')
    return render(request,'signup.html')

def login(request):
    if request.method=="POST":
        lusername=request.POST.get('lusername')
        lpassword=request.POST.get('lpassword')
        user=authenticate(username=lusername,password=lpassword)
        if user is not None:
            authlogin(request,user)
            messages.info(request,"Logged in")
            return redirect("home")
        else:
            messages.info(request,"Retry")
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    authlogout(request)
    return redirect("home")
