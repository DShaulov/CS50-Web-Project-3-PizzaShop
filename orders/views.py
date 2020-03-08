"""
The module responsible for directing the user around the site?!
"""
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Salad, RegularPizza, SicilianPizza, DinnerPlatter, Sub, Topping, Pasta


# Create your views here.
def index(request):
    """return the front page"""
    # check to see if user is logged in
    try:
        logged_in = request.session['username']

    except KeyError:
        logged_in = ""

    context = {
        "logged_in": logged_in,
        "regular_pizzas": RegularPizza.objects.all(),
        "sicillian_pizzas": SicilianPizza.objects.all().order_by("price"),
        "dinner_platters": DinnerPlatter.objects.all(),
        "subs": Sub.objects.all(),
        "toppings": Topping.objects.all(),
        "pastas": Pasta.objects.all(),
        "salads": Salad.objects.all()
    }
    return render(request, 'menu.html', context=context)

def register(request):
    """manage requests to the /register route"""
    if request.method == "POST":

        # enter user into the users table
        user_name = request.POST.get('userName')
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create_user(username=user_name, email=email, password=password,
                                 first_name=first_name, last_name=last_name)

        #TODO upon registering log the user in
        return HttpResponseRedirect("/")

    if request.method =="GET":
        # passing in the logged_in context so that "logout" nav button
        # doesnt render when there is no user
        context = {
            "logged_in": ""
        }
        return render(request, "register.html", context=context)


def login(request):
    """manage requests to the /login route"""
    if request.method == "POST":
        user_name = request.POST.get('userName')
        password = request.POST.get('password')

        # authenticate returns a user object if username and password match
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            request.session['username'] = user.username
            return HttpResponseRedirect("/")
        
        else:
            context = {
                "error": "*username or password are incorrect"
            }
            return render(request, "login.html", context=context)

        return "TODO"

    if request.method == "GET":
        # passing in the logged_in context so that "logout" nav button
        # doesnt render when there is no user
        context = {
            "logged_in": ""
        }
        return render(request, "login.html", context=context)

def logout(request):
    del request.session['username']
    return HttpResponseRedirect("/")
