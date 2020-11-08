from django.db import models
from address.models import Address
from customer_email.models import Email 


class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField()
    phone_number = models.CharField(max_length=10)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    email_id = models.ForeignKey(Email, on_delete=models.CASCADE,default="", editable=False)
    
