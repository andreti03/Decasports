from django.db import models
from products.models import Product
from shopping_cart.models import Shopping_cart

class Cart_product(models.Model):
    cart_product_id = models.IntegerField(primary_key=True)
    amount = models.SmallIntegerField()
    price_total = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Shopping_cart, on_delete=models.CASCADE)

class Backup(models.Model):
    cart_product_id = models.IntegerField(primary_key=True)
    amount = models.SmallIntegerField()
    price_total = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Shopping_cart, on_delete=models.CASCADE)
    total = models.IntegerField()
