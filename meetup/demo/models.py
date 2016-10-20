# -*- coding: utf-8 -*-
from django.db import models
from django.utils.six import python_2_unicode_compatible


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, related_name='products')
    brand = models.ForeignKey('demo.Brand', related_name='products')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class CartItem(models.Model):
    product = models.ForeignKey(Product)

    def __str__(self):
        return str(self.id)


@python_2_unicode_compatible
class Brand(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
