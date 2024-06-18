from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def ourproducts(request):
    return render(request, 'food.html')

def index(request):
    return render(request, 'index.html')

def aboutUs(request):
    return render(request, 'about.html')

def FAQ(request):
    return render(request, 'faq.html')

