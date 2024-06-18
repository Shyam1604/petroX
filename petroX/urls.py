"""
URL configuration for petroX project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from petroX.views import home
from petroX.views import ourproducts
from petroX.views import index
from petroX.views import aboutUs
from petroX.views import FAQ
from app1.views import *
from app1.views import signup
from app1.views import order



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('food.html', ourproducts,name='ourproducts'),
    path('index.html', index,name='index'),
    path('about.html', aboutUs,name='aboutUs'),
    path('faq.html', FAQ,name='FAQ'),
    path('Login.html', Loginpage,name='Loginpage'),
    path('Signup.html', signup,name='signup'),
    path('order1.html', order,name='order'),
    path('order2.html', order2,name='order2'),
    path('order3.html', order3,name='order3'),
    path('order4.html', order4,name='order4'),
    path('invoice.html', invoice,name='invoice'),
    path('order5.html', order5,name='order5'),
    path('order6.html', order6,name='order6'),
]
