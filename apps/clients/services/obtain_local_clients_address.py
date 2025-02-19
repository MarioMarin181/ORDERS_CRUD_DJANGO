from ..models import ClientModel, AddressModel
from ..serializers import ClientSerializer, AddressSerializer

def obtain_local_clients():

    """Retrieves and serializes all clients from the local database.

    This function fetches all clients stored in the local database, serializes them using 
    the `ClientSerializer`, and returns the serialized data. If an error occurs during the 
    retrieval or serialization process, an exception is raised.

    Returns:
        list: A list of serialized client objects.

    Raises:
        Exception: If an error occurs while retrieving or serializing the clients.
    """
    try:
        clients = ClientModel.objects.all()
        serialized_clients = ClientSerializer(clients, many = True)
        return serialized_clients.data
    except Exception as e:
        raise Exception(f"Error durante la obtención y serialización de los clientes locales: {e}")
    
def obtain_local_address():

    """Retrieves and serializes all address from the local database.

    This function fetches all address stored in the local database, serializes them using 
    the `AddressSerializer`, and returns the serialized data. If an error occurs during the 
    retrieval or serialization process, an exception is raised.

    Returns:
        list: A list of serialized address objects.

    Raises:
        Exception: If an error occurs while retrieving or serializing the address.
    """
    try:
        address = AddressModel.objects.all()
        serialized_address = AddressSerializer(address, many = True)
        return serialized_address.data
    except Exception as e:
        raise Exception(f"Error durante la obtención y serialización de las direcciones locales: {e}")