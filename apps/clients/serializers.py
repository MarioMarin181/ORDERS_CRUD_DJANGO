from rest_framework import serializers
from .models import *

class ClientSerializer(serializers.ModelSerializer):
    """Serializer for Client to handle API representation."""

    class Meta:
        model = ClientModel
        fields = "__all__"

class AddressSerializer(serializers.ModelSerializer):
    """Serializer for Address to handle API representation."""

    class Meta:
        model = AddressModel
        fields = "__all__"