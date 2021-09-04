from rest_framework import serializers
from .models import Product, Option, Order


class ProductListSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()

    def get_options(self, obj):
        return OptionListSerializer(obj.option_set.all(), many=True).data

    class Meta:
        model = Product
        fields = ['id', 'title', 'options']


class OptionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        exclude = ('product', )


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
