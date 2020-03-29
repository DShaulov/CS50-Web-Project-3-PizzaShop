from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("checkout", views.checkout, name="cart"),
    path("logOrder", views.logOrder, name="logOrder"),
    path("deleteOrder", views.deleteOrder, name="deleteOrder"),
    path("paidOrder", views.paidOrder, name="paidOrder"),
    path("viewOrders", views.viewOrders, name="viewOrders"),
    path("updateMenu", views.updateMenu, name="updateMenu"),
    path("addNewItem", views.addNewItem, name="addNewItem")
]
