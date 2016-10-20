# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import factory


class CategoryFactory(factory.DjangoModelFactory):
    name = factory.sequence(lambda n: 'category-{}'.format(n))

    class Meta:
        model = 'demo.Category'


class BrandFactory(factory.DjangoModelFactory):
    title = factory.sequence(lambda n: 'brand-{}'.format(n))

    class Meta:
        model = 'demo.Brand'


class ProductFactory(factory.DjangoModelFactory):
    name = factory.sequence(lambda n: 'product-{}'.format(n))

    class Meta:
        model = 'demo.Product'


class CartItemFactory(factory.DjangoModelFactory):

    class Meta:
        model = 'demo.CartItem'
