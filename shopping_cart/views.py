from django.shortcuts import render
from categories.models import Sport

def Home(request):
<<<<<<< HEAD
    return render(request, 'shopping_cart/index.html')

def index(request):
    return render(request, 'shopping_cart/index.html')
=======
    sports = Sport.objects.all()
    context={
        'sport': sports
    }
    return render(request, 'shopping_cart/index.html', context)
>>>>>>> 5f9847c9a587d54331faa05e9bc77d282be37982
