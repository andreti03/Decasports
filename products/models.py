from django.db import models
from categories.models import Sport
from admi.models import Admi


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=30)
    price = models.IntegerField()
    product_sport_id = models.ForeignKey(Sport, on_delete=models.CASCADE)
    admin_id = models.ForeignKey(Admi, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name, self.price
