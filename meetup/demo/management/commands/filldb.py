# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals


from django.core.management.base import BaseCommand, CommandError
from demo.factories import CategoryFactory, ProductFactory, BrandFactory, CartItemFactory
from demo.models import CartItem, Category, Product, Brand


def create_batch(model, count, param='', prefix='', start_with=1, **params):
    items = []
    for i in range(0, count):
        if param:
            params[param] = '{}-{}'.format(prefix, i+start_with)
        items.append(model(**params))
    model.objects.bulk_create(items)
    return items


class Command(BaseCommand):

    def handle(self, *args, **options):

        brands = create_batch(Brand, 30, 'title', 'brand', 30)

        for brand in brands:
            categories = create_batch(Category, 10, 'name', 'brand', 30)
            for category in categories:
                # products = ProductFactory.create_batch(100, category=category, brand=brand)
                products = create_batch(Product, 100, 'name', 'brand', 1000, category=category, brand=brand)

        for product in Product.objects.order_by('?')[:100]:
            CartItemFactory(product=product)
