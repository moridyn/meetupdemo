# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from django.db import connection

from demo.models import CartItem, Product, Category, Brand


class HomeView(TemplateView):
    template_name = 'home.html'


class NotUseIdSmall(TemplateView):
    template_name = 'page.html'

    def get_context_data(self, **kwargs):
        context = super(NotUseIdSmall, self).get_context_data(**kwargs)
        amount = 100
        context['amount'] = amount
        products = Product.objects.order_by('?')[:amount]

        context['items'] = CartItem.objects.filter(product__category_id__in={
            p.category.id for p in products})

        context['queries'] = connection.queries
        return context


class UseIdSmall(TemplateView):
    template_name = 'page.html'

    def get_context_data(self, **kwargs):
        context = super(UseIdSmall, self).get_context_data(**kwargs)
        amount = 100
        context['amount'] = amount
        products = Product.objects.order_by('?')[:amount]

        context['items'] = CartItem.objects.filter(product__category_id__in={
            p.category_id for p in products})

        context['queries'] = connection.queries
        return context


class NotUseId(TemplateView):
    template_name = 'page.html'

    def get_context_data(self, **kwargs):
        context = super(NotUseId, self).get_context_data(**kwargs)
        amount = 1000
        context['amount'] = amount
        products = Product.objects.order_by('?')[:amount]

        context['items'] = CartItem.objects.filter(product__category_id__in={
            p.category.id for p in products})

        context['queries'] = connection.queries
        return context


class UseId(TemplateView):
    template_name = 'page.html'

    def get_context_data(self, **kwargs):
        context = super(UseId, self).get_context_data(**kwargs)
        amount = 1000
        context['amount'] = amount
        products = Product.objects.order_by('?')[:amount]

        context['items'] = CartItem.objects.filter(product__category_id__in={
            p.category_id for p in products})

        context['queries'] = connection.queries
        return context


class NotUseSelectRelated(TemplateView):
    template_name = 'page.html'

    def get_context_data(self, **kwargs):
        context = super(NotUseSelectRelated, self).get_context_data(**kwargs)
        amount = 1000
        context['amount'] = amount
        items = []
        for product in Product.objects.all()[:amount]:
            items.append(
                {'product': product.name, 'category': product.category.name})
        context['items'] = items
        return context


class UseSelectRelated(TemplateView):
    template_name = 'page.html'

    def get_context_data(self, **kwargs):
        context = super(UseSelectRelated, self).get_context_data(**kwargs)
        amount = 1000
        context['amount'] = amount
        items = []
        for product in Product.objects.select_related('category')[:amount]:
            items.append(
                {'product': product.name, 'category': product.category.name})
        context['items'] = items
        return context


class NotUseSelectRelatedBetterCycle(TemplateView):
    template_name = 'page.html'

    def get_context_data(self, **kwargs):
        context = super(NotUseSelectRelatedBetterCycle, self).get_context_data(**kwargs)
        amount = 1000
        context['amount'] = amount
        context['items'] = [
            {'product': product.name, 'category': product.category.name} for product in Product.objects.all()[:amount]]
        return context


class UsePrefetchRelatedNoRender(TemplateView):
    template_name = 'page.html'

    def get_context_data(self, **kwargs):
        context = super(UsePrefetchRelatedNoRender, self).get_context_data(**kwargs)
        amount = 1000
        context['amount'] = amount
        items = []
        for category in Category.objects.prefetch_related('products')[:amount]:
            items.append({'category': category,
                         'products': list(category.products.all()[:amount])})

        list(items)
        return context


class UsePrefetchRelated(TemplateView):
    template_name = 'page.html'

    def get_context_data(self, **kwargs):
        context = super(UsePrefetchRelated, self).get_context_data(**kwargs)
        amount = 1000
        context['amount'] = amount
        items = []
        for category in Category.objects.prefetch_related('products')[:amount]:
            items.append({'category': category,
                         'products': list(category.products.all()[:amount])})

        context['items'] = items
        return context


class NotUsePrefetchRelated(TemplateView):
    template_name = 'page.html'

    def get_context_data(self, **kwargs):
        context = super(NotUsePrefetchRelated, self).get_context_data(**kwargs)
        amount = 1000
        context['amount'] = amount
        items = []
        for category in Category.objects.all()[:amount]:
            items.append({'category': category,
                         'products': list(category.products.all()[:amount])})

        context['items'] = items
        return context


class UsePrefetchRelatedNoRender(TemplateView):
    template_name = 'page.html'

    def get_context_data(self, **kwargs):
        context = super(UsePrefetchRelatedNoRender, self).get_context_data(**kwargs)
        amount = 1000
        context['amount'] = amount
        items = []
        for category in Category.objects.prefetch_related('products')[:amount]:
            items.append({'category': category,
                         'products': list(category.products.all()[:amount])})

        list(items)
        return context


class NotUseBulkCreate(TemplateView):
    template_name = 'page.html'

    def get_context_data(self, **kwargs):
        context = super(NotUseBulkCreate, self).get_context_data(**kwargs)
        amount = 1000
        context['amount'] = amount
        items = []
        category = Category.objects.last()
        brand = Brand.objects.last()
        for i in range(0, amount):
            name = 'test_p {}'.format(i)
            items.append(Product.objects.create(name=name, category=category, brand=brand).id)
        Product.objects.filter(id__in=items).delete()
        return context


class UseBulkCreate(TemplateView):
    template_name = 'page.html'

    def get_context_data(self, **kwargs):
        context = super(UseBulkCreate, self).get_context_data(**kwargs)
        amount = 1000
        context['amount'] = amount
        items = []
        category = Category.objects.last()
        brand = Brand.objects.last()
        for i in range(0, amount):
            name = 'test_p {}'.format(i)
            items.append(Product(name=name, category=category, brand=brand))
        Product.objects.bulk_create(items)
        Product.objects.filter(id__in=[item.id for item in items]).delete()
        return context
