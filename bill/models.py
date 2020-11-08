from django.db import models
from customers.models import Customer
from shopping_cart.models import Shopping_cart



class Bill(models.Model):
    bill_number = models.IntegerField(primary_key=True)
    bill_date = models.DateField()
    total = models.IntegerField()
    customer_id = models.ForeignKey(Customer, on_delete=CASCADE)
    cart_id = models.ForeignKey(Shopping_cart, on_delete=CASCADE)

    def __str__(self):
        return self.bill_number, self.bill_date, self.total

