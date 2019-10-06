from django.contrib import admin
from .models import Categories, Products, Order, OrderItens

admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(OrderItens)

# Register your models here.
