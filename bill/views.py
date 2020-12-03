from django.shortcuts import render
from categories.models import Sport
from products.models import Product
from cart_product.models import Cart_product
from shopping_cart.models import Shopping_cart
from customers.models import Customer
from address.models import Address
from city.models import City
from .models import Bill
from datetime import date

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