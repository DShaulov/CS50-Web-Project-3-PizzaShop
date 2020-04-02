"""
The module responsible for directing the user around the site?!
"""
import time
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Salad, RegularPizza, SicilianPizza, DinnerPlatter, Sub, Topping, Pasta, SubExtra, OrderCart, OrderPaid, SpecialPizza


# Create your views here.
def index(request):
    """return the front page"""
    # check to see if user is logged in
    try:
        logged_in = request.session['username']
        staff_check = User.objects.get(username=logged_in).is_staff
        context = {
        "logged_in": logged_in,
        "regular_pizzas": RegularPizza.objects.all().order_by("price"),
        "sicillian_pizzas": SicilianPizza.objects.all().order_by("price"),
        "dinner_platters": DinnerPlatter.objects.all().order_by("price"),
        "subs": Sub.objects.all().order_by("price").order_by("price"),
        "sub_extras": SubExtra.objects.all(),
        "toppings": Topping.objects.all(),
        "pastas": Pasta.objects.all().order_by("price"),
        "salads": Salad.objects.all().order_by("price"),
        "special_pizzas": SpecialPizza.objects.all().order_by("price"),
        "cart_contents": OrderCart.objects.filter(username = request.session['username']).all(),
        "staff_status": staff_check
    }

    except KeyError:
        logged_in = ""
        context = {
        "logged_in": logged_in,
        "regular_pizzas": RegularPizza.objects.all().order_by("price"),
        "sicillian_pizzas": SicilianPizza.objects.all().order_by("price").order_by("price"),
        "dinner_platters": DinnerPlatter.objects.all().order_by("price").order_by("price"),
        "subs": Sub.objects.all().order_by("price").order_by("price"),
        "sub_extras": SubExtra.objects.all(),
        "toppings": Topping.objects.all(),
        "pastas": Pasta.objects.all().order_by("price"),
        "salads": Salad.objects.all().order_by("price"),
        "special_pizzas": SpecialPizza.objects.all().order_by("price")
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
    """define the checkout route"""
    # check to see if user is logged in
    try:
        logged_in = request.session['username']

    except KeyError:
        return HttpResponseRedirect("/login")
    
    # if logged in, pass along the users cart contents to the checkout page and render the page
    context = {
        "logged_in": logged_in,
        "orders": OrderCart.objects.filter(username=request.session['username']).all()
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
        # arrange the toppings before querying the database
        toppings = request.POST.getlist('selected_topping_array[]')
        toppings_joined = ", ".join(toppings)

        delete_order = OrderCart.objects.filter(
            username = request.session['username'],
            dish_title = request.POST.get('dish_title'),
            dish_type = request.POST.get('dish_type'),
            dish_size = request.POST.get('dish_size'),
            dish_instructions = request.POST.get('textarea_text'),
            dish_price = request.POST.get('dish_price'),
            dish_extra_topping = toppings_joined
        )[:1].get()
        delete_order.delete()
    return HttpResponse("")

def paidOrder(request):
    """defines the paid order route"""
    # select everything from the database that has the same username
    logged_order = OrderCart.objects.filter(username=request.session['username']).all()
    
    
    for i in range(len(logged_order)):
        # for each order, add it to the OrderPaid table
        paid_order = OrderPaid(order=logged_order[i], time_stamp=str(time.localtime().tm_mon) + "-" + str(time.localtime().tm_mday) + "  " \
             + str(time.localtime().tm_hour) + ":" + str(time.localtime().tm_min) + ":" + str(time.localtime().tm_sec))
        paid_order.save()

    # after transfer, delete the order from the OrderCart table
    logged_order.delete()

    context = {
        'logged_in': request.session['username']
    }
    return render(request, 'thankYou.html')

def viewOrders(request):
    """defines the view order route"""
    context = {
        "orders": OrderPaid.objects.all()
    }
    return render(request, "viewOrders.html", context=context)

def updateMenu(request):
    """defines the update menu route"""
    context = {
        "regular_pizzas": RegularPizza.objects.all().order_by("price"),
        "sicillian_pizzas": SicilianPizza.objects.all().order_by("price"),
        "dinner_platters": DinnerPlatter.objects.all().order_by("price"),
        "subs": Sub.objects.all().order_by("price").order_by("price"),
        "sub_extras": SubExtra.objects.all(),
        "toppings": Topping.objects.all(),
        "pastas": Pasta.objects.all().order_by("price"),
        "salads": Salad.objects.all().order_by("price"),
        "special_pizzas": SpecialPizza.objects.all().order_by("price")
    }
    return render(request, 'updateMenu.html', context=context)

def addNewItem(request):
    """defines the add new item to the menu route"""

    # get the menu items to add to the database
    new_item_name = request.POST.get('new_item_name')
    new_item_toppings = request.POST.get('new_item_toppings')
    new_item_price = request.POST.get('new_item_price')
    new_item_category = request.POST.get('new_item_category')

    # add the items to the database
    if new_item_category == "regular_pizza":
        new_item = RegularPizza(
            size = new_item_name,
            toppings = new_item_toppings,
            price = new_item_price
        )
        new_item.save()

    if new_item_category == "sicillian_pizza":
        new_item = SicilianPizza(
            size = new_item_name,
            toppings = new_item_toppings,
            price = new_item_price
        )
        new_item.save()
    
    if new_item_category == "salad":
        new_item = Salad(
            name = new_item_name,
            price = new_item_price
        )
        new_item.save()

    if new_item_category == "dinner_platter":
        new_item = DinnerPlatter(
            name = new_item_name,
            size = new_item_toppings,
            price = new_item_price
        )
        new_item.save()

    if new_item_category == "subs":
        new_item = Sub(
            name = new_item_name,
            price = new_item_price
        )
        new_item.save()

    if new_item_category == "pasta":
        new_item = Pasta(
            name = new_item_name,
            price = new_item_price
        )
        new_item.save()

    if new_item_category == "special_pizza":
        new_item = SpecialPizza(
            name = new_item_name,
            price = new_item_price
        )
        new_item.save()
    
    if new_item_category == "topping":
        new_item = Topping(
            name = new_item_name,
        )
        new_item.save()

    if new_item_category == "sub_extra":
        new_item = SpecialPizza(
            name = new_item_name,
            price = new_item_price
        )
        new_item.save()
    return HttpResponse("")

def removeMenuItem(request):
    """defines the remove menu item path"""
    # get the item info
    remove_id = request.POST.get('remove_id')
    remove_category = request.POST.get('remove_category')



    # remove the item from the database
    if remove_category == "regular_pizza":
        remove_item = RegularPizza.objects.get(
            id = remove_id
        )
        remove_item.delete()


    if remove_category == "sicillian_pizza":
        remove_item = SicilianPizza.objects.get(
            id = remove_id
        )
        remove_item.delete()


    if remove_category == "salad":
        remove_item = Salad.objects.get(
            id = remove_id

        )
        remove_item.delete()


    if remove_category == "dinner_platter":
        remove_item = DinnerPlatter.objects.get(
            id = remove_id
        )
        remove_item.delete()


    if remove_category == "sub":
        remove_item = Sub.objects.get(
            id = remove_id
        )
        remove_item.delete()


    if remove_category == "pasta":
        remove_item = Pasta.objects.get(
            id = remove_id
        )
        remove_item.delete()


    if remove_category == "special_pizza":
        remove_item = SpecialPizza.objects.get(
            id = remove_id
        )
        remove_item.delete()

    if remove_category == "topping":
        remove_item = Topping.objects.get(
            id = remove_id
        )
        remove_item.delete()

    if remove_category == "sub_extra":
        remove_item = SubExtra.objects.get(
            id = remove_id
        )
        remove_item.delete()
    

    
    return HttpResponse("")