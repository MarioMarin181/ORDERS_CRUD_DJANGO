from ..models import ProductModel
from ..serializers import ProductSerializer
from rest_framework.exceptions import NotFound

def update_product(request, id_product):

    try:
        product = ProductModel.objects.get(id_product=id_product)
    except ProductModel.DoesNotExist:
        raise NotFound("Product not found")
    
    data = request.data.copy()
    if "image" in request.FILES:
        data["image"] = request.FILES["image"]
    
    serializer = ProductSerializer(product, data=data, partial=True, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    
    return serializer.errors