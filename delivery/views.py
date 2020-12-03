from django.shortcuts import render, redirect
from customers.models import Customer
from address.models import Address
from city.models import City
from categories.models import Sport
from tradesman.models import Tradesman
from .models import Delivery
from django.contrib import messages

def index(request):
    delivery = Delivery.objects.all()
    tradesman = Tradesman.objects.all()
    customers = Customer.objects.all()
    address = Address.objects.all()
    city = City.objects.all()
    sports = Sport.objects.all()
    context = {
        'delivery':delivery,
        'tradesman':tradesman,
        'customers':customers, 
        'address':address,
        'sport': sports, 
        'city':city
    }
    return render(request, 'delivery/index.html', context)
