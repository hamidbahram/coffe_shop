from rest_framework.response import Response
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Option, Order, OptionValue


class ProductListSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()

    def get_options(self, obj):
        return OptionListSerializer(obj.option_set.all(), many=True).data

    class Meta:
        model = Product
        fields = ['id', 'title', 'options']


class OptionListSerializer(serializers.ModelSerializer):
    value = serializers.SerializerMethodField()

    def get_value(self, obj):
        return OptionValueListSerializer(obj.optionvalue_set.all(), many=True).data

    class Meta:
        model = Option
        fields = ['id', 'ingredients', 'value']


class OptionValueListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionValue
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class OrderListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    product = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    def get_product(self, obj):
        return obj.product.title


    class Meta:
        model = Order
        fields = ('user', 'product')
