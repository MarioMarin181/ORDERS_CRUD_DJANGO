from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .services.get_products import get_all_products
from .services.update_products import update_product
from rest_framework.exceptions import NotFound


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

    return Response(routes, status=status.HTTP_200_OK)

# TODO: Implement view for getting all the products from the database

@api_view(["GET"])
def get_products_database(request):
    """Retrieves all products from the database.

    This endpoint fetches all products stored in the local database 
    and returns them in a serialized format. If an error occurs 
    during retrieval, it returns a server error response.

    Args:
        request (Request): The request object.

    Returns:
        Response: A JSON response containing the list of all products 
                  (HTTP 200 OK) or an error message (HTTP 500 Internal Server Error).
    """
    try:
        products = get_all_products(request)
        return Response(products, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# TODO: Implement view for editing a product in the database
@api_view(["PATCH"])
def product_partial_update(request, id_product):
    """Partially updates a product in WooCommerce and the local database.

    This endpoint updates a product using partial data (`PATCH`). 
    It first attempts to update the product in WooCommerce and then 
    updates the local database. If the product is not found locally 
    but exists in WooCommerce, it is created in the local database.

    Args:
        request (Request): The request object containing the updated product data.
        id_product (int): The ID of the product to be updated.

    Returns:
        Response: A JSON response containing the updated product data (HTTP 200 OK),
                  an error message if the update fails (HTTP 400 Bad Request),
                  a not found error if the product does not exist (HTTP 404 Not Found),
                  or a server error message (HTTP 500 Internal Server Error).
    """
    
    try:
        updated_product = update_product(request, id_product)

        if isinstance(updated_product, dict) and "error" in updated_product:
            return Response(updated_product, status=status.HTTP_400_BAD_REQUEST)

        return Response(updated_product, status=status.HTTP_200_OK)

    except NotFound as e:
        return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

