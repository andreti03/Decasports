from django.shortcuts import render
from django.http import JsonResponse
from categories.models import Sport
from products.models import Product
from cart_product.models import Cart_product
from shopping_cart.models import Shopping_cart
from customers.models import Customer
from address.models import Address
from tradesman.models import Tradesman
from delivery.models import Delivery
from city.models import City
from .models import Bill
from datetime import date
import json
from random import randrange

def Home(request):
    return render(request, 'bill/index.html')

def index(request):
    user = request.user
    bill = Bill.objects.all()
    m=0
    for q in bill:
        if m < q.bill_number:
            m = q.bill_number
    m=m+1
    day = date.today()
    dt = day.strftime("%Y/%m/%d")


    products = Product.objects.all()
    sports = Sport.objects.all()
    cart = Shopping_cart.objects.get(customer_id_id=user.id)
    cart_pro = Cart_product.objects.all()
    customers = Customer.objects.all()
    address = Address.objects.all()
    city = City.objects.all()
    context={
        'dt': dt,
        'bill': bill,
        'sport': sports,
        'customers':customers, 
        'address':address,
        'city':city,
        'cart': cart,
        'products': products,
        'cart_pro': cart_pro,
        'm': m,
    }
    return render(request, 'bill/index.html', context)

def createBill(request):
    user = request.user
    data = json.loads(request.body)
    cartID = data['cartID']
    action = data['action']
    cart = Shopping_cart.objects.get(cart_id=cartID)
    customer = Customer.objects.get(customer_id=cart.customer_id_id)
    tradesman = Tradesman.objects.get(employer_id= randrange(6))
    cart_pro = Cart_product.objects.all()
    total = cart.total
    bill = Bill.objects.all()
    day = date.today()
    dt = day.strftime("%Y-%m-%d")
    m=0
    if len(bill) != 0:
        for q in bill:
            if m < q.bill_number:
                m = q.bill_number
        m=m+1
        print('Bill_number',m)
        print('Date',dt)
        print('Customer',customer)
        print('Cart',cart)
        print('Total',total)
        if action == 'create':
            bill1 = Bill(bill_number = m, bill_date = dt, customer_id = customer, cart_id = cart, total = total)
            delivery1 = Delivery(delivery_id = m,bill_number = bill1,customer_id = customer,employer_id = tradesman,delivery_date = dt)
            for cp in cart_pro:
                if cp.cart_id_id == cart.cart_id:
                    cp.delete()
            cart.total=0
            cart.save()

        bill1.save()
        delivery1.save()
    else:
        m=1
        if action == 'create':
            bill1 = Bill(bill_number = m, bill_date = dt, customer_id = customer, cart_id = cart, total = total)
            delivery1 = Delivery(delivery_id = m,bill_number = bill1,customer_id = customer,employer_id = tradesman,delivery_date = dt)
            for cp in cart_pro:
                if cp.cart_id_id == cart.cart_id:
                    cp.delete()
            cart.total=0
            cart.save()

        bill1.save()
        delivery1.save()

    return JsonResponse('The bill was added', safe= False)