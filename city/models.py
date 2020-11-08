from django.db import models

class City(models.Model):
    city_id = models.IntegerField(primary_key=True)
    city_name = models.CharField(max_length=38)
    country = models.CharField(max_length=38)

