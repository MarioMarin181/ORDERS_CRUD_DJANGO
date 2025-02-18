from rest_framework import serializers
from .models import ProductModel

class ProductSerializer(serializers.ModelSerializer):
    """Serializer for ProductModel to handle API representation."""

    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = ProductModel
        fields = ["id_product", "name", "price", "inventory", "description", "image_url", "created_at", "updated_at"]

    def get_image_url(self, obj):
        request = self.context.get("request") 
        if obj.image:
            if request:  
                return request.build_absolute_uri(obj.image.url)  
            else:
                return obj.image.url  
        return None  
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)  # Asigna nuevos valores a los campos
        instance.save()
        return instance 