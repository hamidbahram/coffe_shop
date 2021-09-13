from rest_framework import status
from django.db import transaction, DatabaseError, IntegrityError
from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from app_coffeshop.models import Product, Option, Order, OptionValue
from app_coffeshop.serializers import(
    ProductListSerializer,
    OptionListSerializer,
    OrderListSerializer,
    OptionValueListSerializer,
    UserSerializer,
)


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self, *args, **kwargs):
        return Product.objects.all()


class OptionListAPIView(generics.ListAPIView):
    serializer_class = OptionListSerializer

    queryset = Option.objects.all()


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


class UserCreate(generics.ListCreateAPIView):
    model = User
    serializer_class = UserSerializer

    def get(self, request):
        data = request.GET
        serializer = UserSerializer(data=data)
        try:
            with transaction.atomic():
                if serializer.is_valid():
                    serializer.validated_data
                    serializer.save()
                    # user = User.objects.create(
                    #     username=serializer.initial_data['username'],
                    #     email=serializer.initial_data['email'],
                    #     password=serializer.initial_data['password']
                    # )
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except DatabaseError:
            context = {"DatabaseError": "database is locked"}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)


class UserOrder(generics.ListCreateAPIView):
    model = Order
    serializer_class = OrderListSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        data = request.GET
        serializer = OrderListSerializer(data=data)
        try:
            with transaction.atomic():
                if serializer.is_valid():
                    serializer.validated_data
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except DatabaseError:
            context = {"DatabaseError": "database is locked"}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)


class CanselOrder(generics.UpdateAPIView):
    queryset = Order.objects.all()
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        instance = self.filter_queryset(self.get_queryset())
        instance = instance.get(pk=request.GET.get('status'))
        instance._status = 5
        instance.save()
        context = {"message": "status updated successfully"}
        return Response(context)
