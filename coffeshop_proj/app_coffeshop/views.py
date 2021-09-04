from django.shortcuts import render
from rest_framework import generics
from app_coffeshop.serializers import ProductListSerializer, OptionListSerializer, OrderListSerializer, OptionValueListSerializer
from app_coffeshop.models import Product, Option, Order, OptionValue


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self, *args, **kwargs):
        return Product.objects.all()


class OptionListAPIView(generics.ListAPIView):
    serializer_class = OptionListSerializer

    def get_queryset(self, *args, **kwargs):
        return Option.objects.all()


class OptionValueListAPIView(generics.ListAPIView):
    serializer_class = OptionValueListSerializer

    def get_queryset(self, *args, **kwargs):
        return OptionValue.objects.all()


class OrderListAPIView(generics.ListAPIView):
    serializer_class = OrderListSerializer

    def get_queryset(self, *args, **kwargs):
        return Order.objects.all()
