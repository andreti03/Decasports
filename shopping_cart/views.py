from django.shortcuts import render
from categories.models import Sport

def Home(request):
    return render(request, 'shopping_cart/index.html')

def index(request):
    return render(request, 'shopping_cart/index.html')
    sports = Sport.objects.all()
    context={
        'sport': sports
    }
    return render(request, 'shopping_cart/index.html', context)
