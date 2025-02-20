from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .services.obtain_local_clients_address import obtain_local_clients, obtain_local_address
# Create your views here.
@api_view(["GET"])
def route_index(request):
    """Returns a list of all available routes.

    Args:
        request (Request): The request object.

    Returns:
        Response: The response object.
    """
    routes = [
        "get_local_clients",
        "get_local_address"
    ]
    return Response(routes, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_local_clients(request):
    """Gets all clients from the database.

    Args:
        request (Request): The request object.

    Returns:
        Response: The response object.
    """

    try:
        serialized_clients = obtain_local_clients()
        return Response(serialized_clients, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(["GET"])
def get_local_address(request):
    """Gets all address from the database.

    Args:
        request (Request): The request object.

    Returns:
        Response: The response object.
    """

    try:
        serialized_address = obtain_local_address()
        return Response(serialized_address, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)