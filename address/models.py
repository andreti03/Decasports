from django.db import models
from city.models import City

class Address(models.Model):
    address_id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=60)
    city_id = models.ForeignKey(City, on_delete=CASCADE)

