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
        return f"{self.size} regular pizza, {self.toppings} toppings, cost: {self.price}$, \n {self.toppingWhich}"

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

    def __str__(self):
        return f"{self.size} {self.name} sub, cost: {self.price}$"

class SubExtra(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.name}"

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


class OrderCart(models.Model):
    """defines cart order class"""
    username = models.CharField(max_length=64)
    dish_title = models.CharField(max_length=64)
    dish_type = models.CharField(max_length=64)
    dish_size = models.CharField(max_length=64)
    dish_extra_topping = models.CharField(max_length=64)
    dish_price = models.CharField(max_length=64)
    dish_instructions = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.username} Ordered: {self.dish_title}, {self.dish_type}, Size: {self.dish_size},\
             With Toppings:  {self.dish_extra_topping}, For: {self.dish_price}, Instructions: {self.dish_instructions}'

class OrderPaid(models.Model):
    """defines the paid order model"""
    username = models.CharField(max_length=64)
    dish_title = models.CharField(max_length=64)
    dish_type = models.CharField(max_length=64)
    dish_size = models.CharField(max_length=64)
    dish_extra_topping = models.CharField(max_length=64)
    dish_price = models.CharField(max_length=64)
    dish_instructions = models.CharField(max_length=64)
    time_ordered = models.IntegerField()

    def __str__(self):
        return f'{self.username} ordered: {self.dish_title}, {self.dish_type}, {self.dish_size}, {self.dish_extra_topping}, \
            {self.dish_price}, {self.dish_instructions}, ordered at: {self.time_ordered}'