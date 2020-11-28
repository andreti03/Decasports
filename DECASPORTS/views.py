from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login, logout

def Home(request):
    return render(request, 'Home/Principal.html')

def Sign_in(request):
    return render(request, 'Home/Sign_in.html')

def Sign_up(request):
    return render(request, 'Home/Sign_up.html')

def registerPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            usuario= form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, F"Bienvenid@ {username}")
            login(request, usuario)
            return redirect('Home') 
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            context = {'form': form}
            return render(request, 'Home/Sign_up.html', context)
    
    context = {'form': form}
    return render(request, 'Home/Sign_up.html', context)


def Sign_out(request):
    logout(request)
    messages.success(request, F"La sesión ha finalizado correctamente.")
    return redirect("Sign_in")
