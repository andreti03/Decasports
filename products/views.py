from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from cart_product.models import Cart_product
from customers.models import Customer
from units_per_size.models import Units_per_size
from categories.models import Sport
from shopping_cart.models import Shopping_cart
import json


def index(request):
    products = Product.objects.all()
    ups = Units_per_size.objects.all()
    sports = Sport.objects.all()
    context={
        'sport': sports,
        'products':products,
        'ups': ups,
    }
    return render(request, 'products/index.html', context)

def updateItem(request):
    user = request.user
    data = json.loads(request.body)
    productID = data['productID']
    action = data['action']
    lista= Cart_product.objects.all()
    m=0

    if len(lista)!=0:
        for i in lista:
            if m < i.cart_product_id:
                m=i.cart_product_id

        customers = Customer.objects.get(customer_id=user.id)
        product = Product.objects.get(product_id=productID)
        cart = Shopping_cart.objects.get(customer_id_id=user.id)
        ci=cart.cart_id
        pi=product.product_id

        for q in lista:
            if q.cart_id_id == ci and q.product_id_id == pi:
                cart_pro = Cart_product.objects.get(cart_id_id=cart.cart_id, product_id_id=product.product_id)
                break
            else:
                cart_pro = Cart_product(cart_product_id = m+1,amount = 0,price_total = product.price,cart_id_id=cart.cart_id, product_id_id=product.product_id)
        
        print(customers)
        print(product)
        print(cart)
        print(cart_pro)
        #Cart_product(cart_product_id = 3,amount = 1,price_total = 50000,product_id = Product3,cart_id= Shopping_cart2)

        if action == 'add':
            cart_pro.amount = (cart_pro.amount + 1)
            cart_pro.price_total = (cart_pro.amount*product.price )
            cart.total = (cart.total+product.price)

        elif action == 'remove':
            cart_pro.amount = (cart_pro.amount - 1)
            cart_pro.price_total = (cart_pro.amount*product.price )
            cart.total = (cart.total-product.price)

        cart_pro.save()
        cart.save()

        if cart_pro.amount <= 0:
            cart_pro.delete()

        return JsonResponse('Item was added', safe= False)
    else:
        cart_pro = Cart_product(cart_product_id = m+1,amount = 0,price_total = product.price,cart_id_id=cart.cart_id, product_id_id=product.product_id)
        
        if action == 'add':
            cart_pro.amount = (cart_pro.amount + 1)
            cart_pro.price_total = (cart_pro.amount*product.price )
            cart.total = (cart.total+product.price)

        elif action == 'remove':
            cart_pro.amount = (cart_pro.amount - 1)
            cart_pro.price_total = (cart_pro.amount*product.price )
            cart.total = (cart.total-product.price)

        cart_pro.save()
        cart.save()

        if cart_pro.amount <= 0:
            cart_pro.delete()


def Home(request):
    return render(request, 'products/index.html')