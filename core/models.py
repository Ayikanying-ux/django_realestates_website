from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
    HOUSES
        -name
        -image
        -description
        -location
        -contact
        -price
        -number of bedrooms
        -
"""

class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    house = models.ForeignKey("House", related_name="comments", on_delete=models.DO_NOTHING)
    comment = models.TextField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.username} comments"


class Agent(models.Model):
    name=models.CharField(max_length=30)
    contact = models.CharField(max_length=13)

    def __str__(self) -> str:
        return self.name

class House(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="house/images")
    description = models.TextField(max_length=500)
    location = models.CharField(max_length=100)
    number_of_bedrooms = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name} house'
