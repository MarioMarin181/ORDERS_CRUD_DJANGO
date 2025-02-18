from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from .models import ProductModel

@api_view(["GET"])
def route_index(request):
    """Returns a list of all available routes.

    Args:
        request (Request): The request object.

    Returns:
        Response: The response object.
    """

    routes = [
        "get_products_database",
        "edit_product"
    ]

    return Response(routes)

# TODO: Implement view for getting all the products from the database

@api_view(["GET"])
def get_products_database(request):
    """Gets all the products in the database"""
    products = ProductModel.objects.all()
    serialized_products = ProductSerializer(products, many=True, context={"request": request})
    return Response(serialized_products.data, status=status.HTTP_200_OK)

# TODO: Implement view for editing a product in the database
@api_view(["PATCH"])
def product_partial_update(request, id_product):
    """Update a single product partially (PATCH)."""
    try:
        product = ProductModel.objects.get(id_product=id_product)
    except ProductModel.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    data = request.data.copy()
    if "image" in request.FILES:
        data["image"] = request.FILES["image"]
    
    serializer = ProductSerializer(product, data=data, partial=True, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
