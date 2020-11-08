from django.db import models

class Sport(models.Model):
    sport_id = models.IntegerField(primary_key=True)
    sport_name = models.CharField(max_length=38)

    def __str__(self):
        return self.sport_name

