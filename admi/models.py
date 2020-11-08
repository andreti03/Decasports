from django.db import models

class Admi(models.Model):
    admi_id = models.IntegerField(primary_key=True)
    admi_name = models.CharField(max_length=38)
    admi_last_name = models.CharField(max_length=38)

