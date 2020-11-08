from django.db import models


class Tradesman(models.Model):
    employer_id = models.IntegerField(primary_key=True)
    dni = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)

