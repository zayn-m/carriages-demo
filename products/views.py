from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import Http404

from .models import Product

from main.views import get_categories

# Create your views here.


class ProductList(ListView):
    template_name = 'products/product_list.html'

    def get_queryset(self):
        category = self.kwargs.get('category')
        slug = self.kwargs.get('slug')

        return Product.objects.filter(category=category.capitalize(), slug=slug)

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        category = self.kwargs.get('category')
        slug = self.kwargs.get('slug')
        title = slug.replace('-', ' ')
        data = {
            'title': title,
            "riding": get_categories('Riding'),
            "driving": get_categories('Driving'),
            "farrier": get_categories('Farrier'),
            "veterinary": get_categories('Veterinary'),
            "object_list": Product.objects.filter(category=category.capitalize(), slug=slug)
        }
        return data


class ProductDetail(DetailView):
    template_name = 'products/product_detail.html'

    def get_object(self, queryset=None):
        item_sku = self.kwargs.get('sku')
        instance = Product.objects.get(sku=item_sku)
        if instance is None:
            raise Http404('Product not found!')
        return instance

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        title = slug.replace('-', ' ')

        data = {
            'title': title,
            "riding": get_categories('Riding'),
            "driving": get_categories('Driving'),
            "farrier": get_categories('Farrier'),
            "veterinary": get_categories('Veterinary'),
            "object": self.get_object()
        }
        return data



