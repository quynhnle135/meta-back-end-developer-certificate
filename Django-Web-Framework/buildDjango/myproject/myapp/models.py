from django.db import models


class Menuitems(models.Model):
    itemname = models.CharField(max_length=200)
    category = models.CharField(max_length=300)
    year = models.IntegerField()

class Drinks(models.Model):
    drink_name = models.CharField(max_length=200)
    price = models.IntegerField()
