from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    country = models.CharField(max_length=64)

class Listing(models.Model):
    title = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{ self.title } { self.price }"

class Bid(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    bid_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")

    def __str__(self):
        return f"{ self.user.first_name } { self.amount }$ { self.bid_date }"

class Comment(models.Model):
    content = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    listing = models.ForeignKey(Bid, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{ self.content } by { self.user.first_name }"
