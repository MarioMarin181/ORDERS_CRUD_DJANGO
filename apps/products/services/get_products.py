from ..models import ProductModel
from ..serializers import ProductSerializer

def get_all_products(request):
    """Gets all the products in the database"""
    products = ProductModel.objects.all()
    return ProductSerializer(products, many=True, context={"request": request}).data