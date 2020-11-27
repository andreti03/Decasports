"""DECASPORTS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.Home, name ='Home'),
    path('login/', LoginView.as_view(template_name= 'Home/Sign_in.html'), name ='Sign_in'),
    path('cr_acc/', views.registerPage, name ='Sign_up'),
    path('admin/', admin.site.urls),
    path('address/', include(('address.urls','address'))),
    path('bill/', include(('bill.urls','bill'))),
    path('categories/', include(('categories.urls','categories'))),
    path('customers/', include(('customers.urls','customers'))),
    path('shopping_cart/', include(('shopping_cart.urls','shopping_cart'))),
    path('products/', include(('products.urls','products')))
]
