"""TD"""
from django.db import models

# Create your models here.
class Salad(models.Model):
    """defines salad object"""
    name = models.CharField(max_length=64)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"{self.name} for {self.price}$"

class Topping(models.Model):
    """defines topping object"""
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class RegularPizza(models.Model):
    """defines regular pizza class"""
    size = models.CharField(null=False, blank=False, max_length=64)
    toppings = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return f"{self.size} regular pizza, {self.toppings} toppings, cost: {self.price}$"

class SicilianPizza(models.Model):
    """defines sicillian pizza class"""
    size = models.CharField(null=False, blank=False, max_length=64)
    toppings = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return f"{self.size} regular pizza, {self.toppings} toppings, cost: {self.price}$"

class Sub(models.Model):
    """defines sub-sandwich class"""
    name = models.CharField(max_length=64)
    size = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def extra_cheese(self, boolean):
        """if extra cheese is given arguement true, add 0.50 to the price"""
        if boolean is True:
            self.price = self.price + 0.50

    def __str__(self):
        return f"{self.size} {self.name} sub, cost: {self.price}$"

class Pasta(models.Model):
    """defines pasta class"""
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} pasta, cost: {self.price}$"

class DinnerPlatter(models.Model):
    """defines dinner platter class"""
    name = models.CharField(max_length=64)
    size = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.size} {self.name} dinner platter, cost: {self.price}$"
