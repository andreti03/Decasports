from django.db import models
from bill.models import Bill
from customers.models import Customer
from tradesman.models import Tradesman


class Delivery(models.Model):
    delivery_id = models.IntegerField(primary_key=True)
    delivery_date = models.DateField()
    bill_number = models.ForeignKey(Bill, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employer_id = models.ForeignKey(Tradesman, on_delete=models.CASCADE)
