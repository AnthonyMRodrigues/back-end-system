from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
    deleted_at = models.TimeField()


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
    deleted_at = models.TimeField()
    category_id = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    usd_price = models.DecimalField(decimal_places=2, max_digits=15)
    real_price = models.DecimalField(decimal_places=2, max_digits=15)
    euro_price = models.DecimalField(decimal_places=2, max_digits=15)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
    deleted_at = models.TimeField()


class OrderItens(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
    usd_price = models.DecimalField(decimal_places=2, max_digits=15)
    real_price = models.DecimalField(decimal_places=2, max_digits=15)
    euro_price = models.DecimalField(decimal_places=2, max_digits=15)
    order_id = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
