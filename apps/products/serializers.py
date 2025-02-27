from rest_framework import serializers
from .models import ProductModel

class ProductSerializer(serializers.ModelSerializer):
    """Serializer for ProductModel to handle API representation."""
    
    class Meta:
        model = ProductModel
        fields = "__all__" 
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)  # Asigna nuevos valores a los campos
        instance.save()
        return instance 