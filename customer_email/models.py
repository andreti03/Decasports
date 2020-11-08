from django.db import models

class Email(models.Model):
    email_id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=30)
    e_password = models.CharField(max_length=80)
