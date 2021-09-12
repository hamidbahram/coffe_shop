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
    CanselOrderSerializer
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
    serializer_class = CanselOrderSerializer
    permission_classes = (IsAuthenticated,)

    def update(self, request):
        serializer = CanselOrderSerializer(data=request.GET)
        try:
            order = Order.objects.get(id=request.GET.get('order'))
            if serializer.is_valid():
                order._status = 5
                order.save()
                return Response({"message": "status updated successfully"})
            return Response({"message": "failed", "details": serializer.errors})
        except Order.DoesNotExist:
            return Response({"message": "DoesNotExist"})
