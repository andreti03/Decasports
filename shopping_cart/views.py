from django.shortcuts import render
from categories.models import Sport

def Home(request):
    sports = Sport.objects.all()
    context={
        'sport': sports
    }
    return render(request, 'shopping_cart/index.html', context)