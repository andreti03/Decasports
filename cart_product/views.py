from django.shortcuts import render
from products.models import Product
from.cart import Cart
# Create your views here.

def add_product(request,product_id)
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    