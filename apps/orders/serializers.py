from rest_framework import serializers
from apps.products.serializers import ProductSerializer
from apps.clients.serializers import ClientSerializer, AddressSerializer
from .models import *

class OrderItemSerializer(serializers.ModelSerializer):
     """Serializer for OrderItem to handle API representation."""

     product = ProductSerializer()

     class Meta:
         model = OrderItemModel
         fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    """Serializer for Order to handle API representation."""
    
    client = ClientSerializer()
    address = AddressSerializer()
    items = OrderItemSerializer(many=True)

    class Meta:
        model = OrderModel
        fields = "__all__"