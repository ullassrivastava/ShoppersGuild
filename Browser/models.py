from __future__ import unicode_literals
from django.db import models
# Create your models here.
from django.db import models


class Shopper_database(models.Model):
    username = models.CharField(max_length=10, blank=False)
    password = models.CharField(max_length=10, blank=False)
    email = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.username


class Item_database(models.Model):
    items = models.CharField(max_length=10, blank=False)
    price = models.CharField(max_length=3, blank=False)


    def __str__(self):
        return self.total
