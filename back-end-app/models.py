from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
    deleted_at = models.TimeField(null=True, blank=True)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200,blank=True)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
    deleted_at = models.TimeField(null=True, blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    price = models.DecimalField(decimal_places=2, max_digits=15)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
    deleted_at = models.TimeField(null=True, blank=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=15)


class OrderItem(models.Model):
    BRAZILIAN_REAL = 1
    AMERICAN_DOLLAR = 2
    EURO = 3

    currency_types = [
        (BRAZILIAN_REAL, 'Brazilian Real'),
        (AMERICAN_DOLLAR, 'American Dollar'),
        (EURO, 'Euro'),
    ]

    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
    deleted_at = models.TimeField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=15)
    order_id = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    exchange_rate = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    currency = models.IntegerField(max_length=5, choices=currency_types, default=BRAZILIAN_REAL)
