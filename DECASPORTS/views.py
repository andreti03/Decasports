from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from .forms import CreateUserForm


def Home(request):
    return render(request, 'Home/Principal.html')

def Sign_in(request):
    if request.method=='POST':
        form = AuthenticationForm(request, data = request.POST) 
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, F"Bienvenid@ de nuevo {username}!")
                return redirect('Home') 
            else:
                messages.error(request, "Los datos ingresados son incorrectos")
        else:
            messages.error(request, "Los datos ingresados son incorrectos")

    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'Home/Sign_in.html', context)

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
