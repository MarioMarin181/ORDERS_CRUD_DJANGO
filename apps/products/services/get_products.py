from ..models import ProductModel
from ..serializers import ProductSerializer

def get_all_products(request):
    """Gets all the products in the database"""
    
    try:
        products = ProductModel.objects.all()
        return ProductSerializer(products, many=True, context={"request": request}).data
    except Exception as e:
        raise Exception(f"Error al obtener todos los productos desde la base de datos local: {e}")