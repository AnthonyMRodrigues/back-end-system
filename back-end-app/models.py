from django.db import models

# Create your models here.


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
    deleted_at = models.TimeField()


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
    deleted_at = models.TimeField()
    category_id = models.ForeignKey(Categories, on_delete=models.PROTECT)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
