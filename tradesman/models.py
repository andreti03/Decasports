from django.db import models
from django.contrib.auth.models import User 
from admi.models import Admi


class Tradesman(models.Model):
    employer_id = models.IntegerField(primary_key=True)
    dni = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    auth_user_id = models.ForeignKey(User, on_delete=models.CASCADE,default="", editable=False)

    def __str__(self):
        return self.dni

