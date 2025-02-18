from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .services.get_products import get_all_products
from .services.update_products import update_product


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
    products = get_all_products(request)
    return Response(products, status=status.HTTP_200_OK)

# TODO: Implement view for editing a product in the database
@api_view(["PATCH"])
def product_partial_update(request, id_product):
    """Update a single product partially (PATCH)."""
    
    updated_product = update_product(request, id_product)

    if isinstance(updated_product, dict) and "error" in updated_product:
        return Response(updated_product, status=status.HTTP_400_BAD_REQUEST)

    return Response(updated_product, status=status.HTTP_200_OK)

