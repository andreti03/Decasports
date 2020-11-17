from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def Home(request):
    return render(request, 'Home/Principal.html')

def Sign_in(request):
    return render(request, 'Home/Sign_in.html')

def Sign_up(request):
    return render(request, 'Home/Sign_up.html')

def registerPage(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form': form}
    return render(request, 'Home/register.html', context)