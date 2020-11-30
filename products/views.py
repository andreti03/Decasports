from django.shortcuts import render
from .models import Product
from units_per_size.models import Units_per_size
from categories.models import Sport

def index(request):
    products = Product.objects.all()
    ups = Units_per_size.objects.all()
    sports = Sport.objects.all()
    context={
        'sport': sports,
        'products':products,
        'ups': ups
    }
    return render(request, 'products/index.html', context)

def Home(request):
    return render(request, 'products/index.html')