from django.db import models
import random, os
from django.db.models.signals import pre_save

from slugify import slugify


# Create your models here.

CHOICES = (
    ('Riding', 'Riding'),
    ('Driving', 'Driving'),
    ('Farrier', 'Farrier'),
    ('Veterinary', 'Veterinary'),
)


def get_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def image_path(instance, filename):
    new_filename = random.randint(0, 1231245312159)
    name, ext = get_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'products/{new_filename}{final_filename}'


class Category(models.Model):
    category = models.CharField(max_length=60, choices=CHOICES)
    sub_category = models.CharField(max_length=80)

    def __str__(self):
        return self.category


class Product(models.Model):
    title = models.CharField(max_length=120)
    sku = models.CharField(max_length=60, unique=True)
    category = models.CharField(max_length=60, choices=CHOICES)
    sub_category = models.CharField(max_length=80)
    slug = models.SlugField(null=True, blank=True)
    desc = models.TextField()
    image = models.ImageField(upload_to=image_path, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


def product_pre_save(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.sub_category)


pre_save.connect(product_pre_save, sender=Product)

