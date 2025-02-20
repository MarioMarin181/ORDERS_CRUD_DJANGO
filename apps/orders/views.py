from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .services.fetch_save_orders import fetch_and_save_orders
from .services.obtain_local_orders import obtain_local_orders


@api_view(["GET"])
def route_index(request):
    """Returns a list of all available routes.

    Args:
        request (Request): The request object.

    Returns:
        Response: The response object.
    """
    routes = [
        "get_orders_woocommerce",
        "get_local_orders"
    ]
    return Response(routes, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_orders_woocommerce(request):
    """Gets all orders from the WooCommerce API and creates them in the database.

    Args:
        request (Request): The request object.

    Returns:
        Response: The response object.
    """
    # TODO: Make a request to the WooCommerce API to get all orders and create them in the database.
    # The creation of the orders should include OrderModel, OrderItemModel, ClientModel and AddressModel objects.
    # The method make_woocommerce_request would be useful for making the request to the WooCommerce API.
    # Use the endpoint 'orders' to get all orders from WooCommerce.

    try:
        data = fetch_and_save_orders()
        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["GET"])
def get_local_orders(request):
    """Gets all orders from the database.

    Args:
        request (Request): The request object.

    Returns:
        Response: The response object.
    """
    # TODO: Create a serializer for the OrderModel and return the serialized data.
    # The serializer should include the OrderModel, OrderItemModel, ClientModel and AddressModel objects.

    try:
        serialized_orders = obtain_local_orders()
        return Response(serialized_orders, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
