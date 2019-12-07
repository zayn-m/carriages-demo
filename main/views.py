from django.shortcuts import render, redirect
from django.views.generic import View

from products.models import Category
from slugify import slugify


def get_categories(title):
    items = []

    for cat in Category.objects.filter(category=title).values('sub_category'):
        items.append({
            "title": cat['sub_category'],
            "slug": slugify(cat['sub_category'])
        })

    return items


def home_page(request):

    context = {
        "riding": get_categories('Riding'),
        "driving": get_categories('Driving'),
        "farrier": get_categories('Farrier'),
        "veterinary": get_categories('Veterinary'),
    }
    return render(request, "index.html", context)


def about_page(request):
    context = {
        "riding": get_categories('Riding'),
        "driving": get_categories('Driving'),
        "farrier": get_categories('Farrier'),
        "veterinary": get_categories('Veterinary'),
    }
    return render(request, "about.html", context)


def contact_page(request):
    context = {
        "riding": get_categories('Riding'),
        "driving": get_categories('Driving'),
        "farrier": get_categories('Farrier'),
        "veterinary": get_categories('Veterinary'),
    }
    return render(request, "contact.html", context)
