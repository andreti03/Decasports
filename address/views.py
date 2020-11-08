from django.shortcuts import render


def Home(request):
    return render(request, 'address/index.html')