from django.db import models


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
