"""
The module responsible for directing the user around the site?!
"""
from django.http import HttpResponse
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
    return render(request, 'menu.html', context=context)

def register(request):
    """return the register.html template"""
    if request.method == "POST":
        return HttpResponse("hehe")

    return render(request, "register.html")


def login(request):
    """return the login.html template"""
    return render(request, "login.html")
