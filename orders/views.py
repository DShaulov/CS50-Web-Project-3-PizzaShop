"""
The module responsible for directing the user around the site?!
"""
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Salad, RegularPizza, SicilianPizza, DinnerPlatter, Sub, Topping, Pasta, SubExtra, OrderCart, OrderPaid


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
        "dinner_platters": DinnerPlatter.objects.all().order_by("price"),
        "subs": Sub.objects.all().order_by("price"),
        "sub_extras": SubExtra.objects.all(),
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
            print("correct")
            request.session['username'] = user.username
            return HttpResponseRedirect("/")
        
        else:
            context = {
                "logged_in": "",
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
    """clear session['username'] and redriect to homepage """
    del request.session['username']
    return HttpResponseRedirect("/")

def checkout(request):
   
    # check to see if user is logged in
    try:
        logged_in = request.session['username']

    except KeyError:
        return HttpResponseRedirect("/login")
    
    context = {
        "logged_in": logged_in
    }
    return render(request, "cart.html", context=context)

def logOrder(request):
    """contains instructions for insering new orders to the database"""
    if request.method == "POST":
        # arrange the toppings before submmiting them to the database
        toppings = request.POST.getlist('selected_topping_array[]')
        toppings_joined = ", ".join(toppings)
        
        new_order = OrderCart(
            username = request.session['username'],
            dish_title = request.POST.get('dish_title'),
            dish_type = request.POST.get('dish_type'),
            dish_size = request.POST.get('dish_size'),
            dish_instructions = request.POST.get('textarea_text'),
            dish_price = request.POST.get('dish_price'),
            dish_extra_topping = toppings_joined
        )

        new_order.save()

        return HttpResponse("")

def deleteOrder(request):
    """contains instructions for deleting an order from the database"""
    if request.method == "POST":
        print("hey in trying to delete this thing!")
        print(request.POST.get('dish_title'))
        print(request.POST.get('dish_size'))
        print(request.POST.get('dish_price'))
        print(request.POST.get('textarea_text'))
        print(request.POST.getlist('selected_topping_array[]'))
        print(request.session["username"])


    return HttpResponse("")