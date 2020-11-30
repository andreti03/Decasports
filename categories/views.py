from django.shortcuts import render
from products.models import Product
from units_per_size.models import Units_per_size
from .models import Sport

def Home(request):
    products = Product.objects.all()
    ups = Units_per_size.objects.all()
    sports = Sport.objects.all()
    context={
        'sport': sports,
        'products':products,
        'ups': ups
    }
    return render(request, 'categories/index.html', context)

def Futbol(request):
    products = Product.objects.all()
    ups = Units_per_size.objects.all()
    Sports = Sport.objects.get(sport_name = 'Futbol')
    sports = Sport.objects.all()
    context={
        'Sport': Sports,
        'sport': sports,
        'products':products,
        'ups': ups
    }
    return render(request, 'categories/index.html', context)

def Basketball(request):
    products = Product.objects.all()
    ups = Units_per_size.objects.all()
    Sports = Sport.objects.get(sport_name = 'Basketball')
    sports = Sport.objects.all()
    context={
        'Sport': Sports,
        'sport': sports,
        'products':products,
        'ups': ups
    }
    return render(request, 'categories/index.html', context)

def Ping(request):
    products = Product.objects.all()
    ups = Units_per_size.objects.all()
    Sports = Sport.objects.get(sport_name = 'Ping-Pong')
    sports = Sport.objects.all()
    context={
        'Sport': Sports,
        'sport': sports,
        'products':products,
        'ups': ups
    }
    return render(request, 'categories/index.html', context)

def Natacion(request):
    products = Product.objects.all()
    ups = Units_per_size.objects.all()
    Sports = Sport.objects.get(sport_name = 'Natación')
    sports = Sport.objects.all()
    context={
        'Sport': Sports,
        'sport': sports,
        'products':products,
        'ups': ups
    }
    return render(request, 'categories/index.html', context)

def Boxeo(request):
    products = Product.objects.all()
    ups = Units_per_size.objects.all()
    Sports = Sport.objects.get(sport_name = 'Boxeo')
    sports = Sport.objects.all()
    context={
        'Sport': Sports,
        'sport': sports,
        'products':products,
        'ups': ups
    }
    return render(request, 'categories/index.html', context)

def Taekwondo(request):
    products = Product.objects.all()
    ups = Units_per_size.objects.all()
    Sports = Sport.objects.get(sport_name = 'Taekwondo')
    sports = Sport.objects.all()
    context={
        'Sport': Sports,
        'sport': sports,
        'products':products,
        'ups': ups
    }
    return render(request, 'categories/index.html', context)

def Atletismo(request):
    products = Product.objects.all()
    ups = Units_per_size.objects.all()
    Sports = Sport.objects.get(sport_name = 'Atletismo')
    sports = Sport.objects.all()
    context={
        'Sport': Sports,
        'sport': sports,
        'products':products,
        'ups': ups
    }
    return render(request, 'categories/index.html', context)

def Ciclismo(request):
    products = Product.objects.all()
    ups = Units_per_size.objects.all()
    Sports = Sport.objects.get(sport_name = 'Ciclismo')
    sports = Sport.objects.all()
    context={
        'Sport': Sports,
        'sport': sports,
        'products':products,
        'ups': ups
    }
    return render(request, 'categories/index.html', context)
