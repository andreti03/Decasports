from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.template.response import TemplateResponse
from categories.models import Sport
from products.models import Product
from cart_product.models import Cart_product, Backup
from shopping_cart.models import Shopping_cart
from customers.models import Customer
from address.models import Address
from tradesman.models import Tradesman
from delivery.models import Delivery
from city.models import City
from bill.models import Bill
import json

def index(request):
    user = request.user
    delivery = Delivery.objects.all()
    tradesman = Tradesman.objects.get(auth_user_id_id=user.id)
    customers = Customer.objects.all()
    address = Address.objects.all()
    city = City.objects.all()
    sports = Sport.objects.all()
    bills = Bill.objects.all()
    context = {
        'bills': bills,
        'delivery':delivery,
        'tradesman':tradesman,
        'customers':customers, 
        'address':address,
        'sport': sports, 
        'city':city
    }
    return render(request, 'delivery/index.html', context)

def backup(request):
    user = request.user
    # data = json.loads(request.body)
    # productID = data['cartID']
    # action = data['action']
    # print('cartID', productID)
    # print('action',action)
    delivery = Delivery.objects.all()
    tradesman = Tradesman.objects.get(auth_user_id_id=user.id)
    cart = Shopping_cart.objects.all()
    customers = Customer.objects.all()
    backup = Backup.objects.all()
    address = Address.objects.all()
    city = City.objects.all()
    sports = Sport.objects.all()
    products = Product.objects.all()
    # bill = Bill.objects.get(bill_number=productID)
    context = {
        'backup':backup,
        'cart':cart,
        'delivery':delivery,
        'tradesman':tradesman,
        'customers':customers, 
        'products': products,
        'address':address,
        'sport': sports, 
        'city':city
    }
    #pag=TemplateResponse(request, 'delivery/billbk.html', context)
    #pag.render()
    return render(request, 'delivery/billbk.html', context)
    #return JsonResponse('Item was added', safe= False)
