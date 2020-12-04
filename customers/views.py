from django.shortcuts import render, redirect
from .models import Customer
from address.models import Address
from city.models import City
from categories.models import Sport
from tradesman.models import Tradesman
from .forms import Update_customer, Update_address
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

def index(request):
    tradesman = Tradesman.objects.all()
    customers = Customer.objects.all()
    address = Address.objects.all()
    city = City.objects.all()
    sports = Sport.objects.all()
    context = {
        'tradesman':tradesman,
        'customers':customers, 
        'address':address,
        'sport': sports, 
        'city':city
    }
    return render(request, 'customers/index.html', context)

def Home(request):
    return render(request, 'customers/index.html')

def formulario(request):
    form = Update_customer(request.POST)
    form2 = Update_address(request.POST)
    user = request.user
    if request.method=='POST':
        if form.is_valid() and form2.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            birthdate = form.cleaned_data.get('birthdate')
            phone_number = form.cleaned_data.get('phone_number')
            address = form2.cleaned_data.get('address')
            up_customer = Customer.objects.get(customer_id = user.id)
            up_customer.first_name = first_name
            up_customer.last_name = last_name
            up_customer.birthdate = birthdate
            up_customer.phone_number = phone_number
            up_address = Address.objects.get(address_id = up_customer.customer_id)
            up_address.address = address
            up_customer.save()
            up_address.save()
            messages.success(request, F"{user.username} tus datos han sido actualizados satisfatoriamente!")
            return redirect('Home')
        else:
             messages.error(request, "Los datos ingresados son incorrectos")

    return render(request, 'customers/encuesta.html', {'form': form, 'form2':form2})
