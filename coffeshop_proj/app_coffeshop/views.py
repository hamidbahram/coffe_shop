from django.shortcuts import render
from rest_framework import generics
from app_coffeshop.serializers import ProductListSerializer
from app_coffeshop.models import Product


class PostListAPIView(generics.ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self, *args, **kwargs):
        return Product.objects.all()
