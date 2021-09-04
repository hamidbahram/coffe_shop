from django.contrib import admin
from .models import Product, Option, Order, OptionValue


admin.site.register(Product)
admin.site.register(Option)
admin.site.register(OptionValue)
admin.site.register(Order)
