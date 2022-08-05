from django.shortcuts import render
from categories.models import Sport
from products.models import Product
from cart_product.models import Cart_product
from .models import Shopping_cart

def Home(request):
    return render(request, 'shopping_cart/index.html')

def index(request):
    user = request.user
    products = Product.objects.all()
    sports = Sport.objects.all()
    cart = Shopping_cart.objects.get(customer_id_id=user.id)
    cart_pro = Cart_product.objects.all()
    context={
        'sport': sports,
        'cart': cart,
        'products': products,
        'cart_pro': cart_pro,
    }
    return render(request, 'shopping_cart/index.html', context)
