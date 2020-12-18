from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    creation_date = models.DateTimeField()

    def __str__(self):
        return f"{ self.title } { self.price }"

class Bid(models.Model):
    pass

class Comment(models.Model):
    pass

