from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from .forms import CreateUserForm, Create_customer, Create_address, Create_city
from categories.models import Sport
from customers.models import Customer
from address.models import Address
from city.models import City
from shopping_cart.models import Shopping_cart
from datetime import date

def Home(request):
    sports = Sport.objects.all()
    context={'sport': sports}
    return render(request, 'Home/Principal.html', context)

def Sign_in(request):
    sports = Sport.objects.all()
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
    context = {
        'form': form,
        'sport': sports
    }
    return render(request, 'Home/Sign_in.html', context)

def Sign_up(request):
    return render(request, 'Home/Sign_up.html')

def registerPage(request):
    form = CreateUserForm()
    form_customer = Create_customer(request.POST)
    form_address = Create_address(request.POST)
    form_city = Create_city(request.POST)
    sports = Sport.objects.all()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid() and form_customer.is_valid() and form_address.is_valid() and form_city.is_valid():
            usuario = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, F"Bienvenid@ {username}")
            login(request, usuario)
            
            user = request.user

            first_name1 = form_customer.cleaned_data.get('first_name')
            last_name1 = form_customer.cleaned_data.get('last_name')
            birthdate1 = form_customer.cleaned_data.get('birthdate')
            phone_number1 = form_customer.cleaned_data.get('phone_number')
            address1 = form_address.cleaned_data.get('address')
            city1 = form_city.cleaned_data.get('city_name')
            country1 = form_city.cleaned_data.get('country')

            city_created = City.objects.get(city_name = city1)

            lista = Address.objects.all()
            m = 0

            for q in lista:
                m += 1

            address_created = Address(address_id = m+1, address = address1, city_id = city_created)
            address_created.save()

            customer_created = Customer(customer_id = user.id,
                                        first_name = first_name1,
                                        last_name = last_name1,
                                        birthdate = birthdate1,
                                        phone_number = phone_number1,
                                        address_id = address_created,
                                        auth_user_id = user)
            customer_created.save()

            lista_shop = Shopping_cart.objects.all()
            count = 0
            for i in lista_shop:
                count += 1
            
            day = date.today()
            dt = day.strftime("%Y-%m-%d")
            shopping_cart_crated = Shopping_cart(cart_id =count+1, effective_date = dt,  total = 0, customer_id = customer_created)
            shopping_cart_crated.save()
            return redirect('Home') 
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            context = {'form': form, 'form_customer': form_customer, 'form_address': form_address, 'form_city': form_city, 'sport': sports}
            return render(request, 'Home/Sign_up.html', context)
    
    context = {'form': form, 'form_customer': form_customer, 'form_address': form_address, 'form_city': form_city, 'sport': sports}
    return render(request, 'Home/Sign_up.html', context)


def Sign_out(request):
    logout(request)
    messages.success(request, F"La sesión ha finalizado correctamente.")
    return redirect("Sign_in")
