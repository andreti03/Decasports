from django.shortcuts import render

def Home(request):
    return render(request, 'Home/Principal.html')


def Sign_in(request):
    return render(request, 'Home/Sign_in.html')

def Sign_up(request):
    return render(request, 'Home/Sign_up.html')