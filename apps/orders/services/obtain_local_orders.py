from ..models import OrderModel
from ..serializers import OrderSerializer

def obtain_local_orders():

    """Retrieves and serializes all orders from the local database.

    This function fetches all orders stored in the local database, serializes them using 
    the `OrderSerializer`, and returns the serialized data. If an error occurs during the 
    retrieval or serialization process, an exception is raised.

    Returns:
        list: A list of serialized order objects.

    Raises:
        Exception: If an error occurs while retrieving or serializing the orders.
    """
    try:
        orders = OrderModel.objects.all()
        serialized_orders = OrderSerializer(orders, many = True)
        return serialized_orders.data
    except Exception as e:
        raise Exception(f"Error durante la obtención y serialización de los pedidos locales: {e}")