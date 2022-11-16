from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length = 64)
    description = models.TextField()
    price = models.IntegerField()
    image = models.CharField(max_length = 64)

    def __str__(self):
        return f"{self.title} and {self.description} and {self.price} and {self.image}"

# class Add_action(models.ModelForm):
#     class Meta:
#         model = Auction_Listing
#         fields = ['title', 'description','price']
