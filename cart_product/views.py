from django.shortcuts import render , redirect 
from products.models import Product
from.apps import Cart
# Create your views here.

def add_product(request,product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    return redirect("index")

def remove_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.remove(product)
    return redirect("index")

def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect("index")

