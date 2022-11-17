from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    pass

class Listing(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length = 64)
    description = models.TextField()
    price = models.IntegerField()
    image = models.CharField(max_length = 64)

    def __str__(self):
        return f"{self.title} \n {self.description} \n {self.price} \n {self.image}\n"

class Bids(models.Model):
    id = models.BigAutoField(primary_key=True)
    # a bid has many to one relation (many bids horen by 1 listing)
    #user = modeBols.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    new_bid = models.IntegerField()

    def __str__(self):
        return f"{self.new_bid}"

class Comments(models.Model):
    id = models.BigAutoField(primary_key=True)
    #user = model.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    new_comment = models.TextField()

    def __str__(self):
        return f"{self.new_comment}"
