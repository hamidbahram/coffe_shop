from django.shortcuts import render
from rest_framework import generics
from app_coffeshop.serializers import ProductListSerializer, OptionListSerializer, OrderListSerializer, OptionValueListSerializer, UserSerializer
from app_coffeshop.models import Product, Option, Order, OptionValue
from django.contrib.auth.models import User



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


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self, *args, **kwargs):
        return User.objects.all()




from django.db import transaction
from rest_framework import status
from rest_framework.response import Response



class UserCreate(generics.ListCreateAPIView):
    model = User
    serializer_class = UserSerializer
    
    def get(self, *args, **kwargs):
        data = self.request.GET
        serializer = UserSerializer(data=data)

        with transaction.atomic():
            if serializer.is_valid():
                user = User.objects.create(
                    username=serializer.initial_data['username'], 
                    email=serializer.initial_data['email'],
                    password=serializer.initial_data['password']
                )
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
