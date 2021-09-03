from rest_framework import serializers
from .models import Product, Option, Order


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class OptionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = "__all__"
        # fields = ("product","ingredients")


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
