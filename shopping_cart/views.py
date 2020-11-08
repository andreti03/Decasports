from django.shortcuts import render

def Home(request):
    return render(request, 'shopping_cart/index.html')