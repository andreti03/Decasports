from django.db import models
from customers.models import Customer


class Shopping_cart(models.Model):
    cart_id = models.IntegerField(primary_key=True)
    effective_date = models.DateField()
    total = models.IntegerField()
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

