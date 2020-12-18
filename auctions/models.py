from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing():
    title = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    creation_date = models.DateTimeField()

class Bid():
    pass

class Comment():
    pass

