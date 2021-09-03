from django.contrib import admin
from .models import Product, Option, Order


admin.site.register(Product)
admin.site.register(Option)
admin.site.register(Order)
