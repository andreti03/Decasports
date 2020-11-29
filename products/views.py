from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products':products})

def Home(request):
    return render(request, 'products/index.html')