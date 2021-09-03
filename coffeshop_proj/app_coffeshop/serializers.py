from rest_framework.serializers import ModelSerializer
from .models import Product, Option, Order

class ProductListSerializer(ModelSerializer):
    class Meta:
        model  = Product
        fields = "__all__"