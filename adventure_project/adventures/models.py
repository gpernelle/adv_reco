from django.db import models
from django.db.models import Count


# Create your models here.
class Adventure(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    kids = models.BooleanField()
    adrenalin = models.IntegerField()
    promoted = models.BooleanField()

    def __str__(self):
        return self.name

