from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not same !!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('Login.html')

    return render (request, 'Signup.html')

def Loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('order1.html')
        else:
            return HttpResponse("username and password is invalid!!")

    return render (request, 'Login.html')

def order(request):
    return render (request, 'order1.html')

def order2(request):
    return render (request, 'order2.html')

def order3(request):
    return render (request, 'order3.html')

def order4(request):
    return render (request, 'order4.html')

def invoice(request):
    return render (request, 'invoice.html')

def order5(request):
    return render (request, 'order5.html')

def order6(request):
    return render (request, 'order6.html')