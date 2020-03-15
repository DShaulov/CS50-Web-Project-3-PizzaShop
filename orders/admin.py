"""TD"""
from django.contrib import admin

from .models import Salad, Topping, RegularPizza, SicilianPizza, Sub, Pasta, DinnerPlatter, OrderCart, SubExtra, OrderPaid, SpecialPizza

# Register your models here.
admin.site.register(Salad)
admin.site.register(Topping)
admin.site.register(RegularPizza)
admin.site.register(SicilianPizza)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(DinnerPlatter)
admin.site.register(SubExtra)
admin.site.register(OrderCart)
admin.site.register(OrderPaid)
admin.site.register(SpecialPizza)