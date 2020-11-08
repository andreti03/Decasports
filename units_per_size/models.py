from django.db import models
from products.models import Product


class Units_per_size(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    xs_units = models.IntegerField()
    s_units = models.IntegerField()
    m_units = models.IntegerField()
    l_units = models.IntegerField()    
    xl_units = models.IntegerField()
    na_units =models.IntegerField()