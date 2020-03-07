"""
The module responsible for directing the user around the site?!
"""

from django.shortcuts import render
from .models import Salad, RegularPizza, SicilianPizza, DinnerPlatter, Sub, Topping, Pasta

# Create your views here.
def index(request):
    """return the front page"""
    context = {
        "regular_pizzas": RegularPizza.objects.all(),
        "sicillian_pizzas": SicilianPizza.objects.all(),
        "dinner_platters": DinnerPlatter.objects.all(),
        "subs": Sub.objects.all(),
        "toppings": Topping.objects.all(),
        "pastas": Pasta.objects.all(),
        "salads": Salad.objects.all()
    }
    return render(request, 'index.html', context=context)
