from apps.clients.models import ClientModel, AddressModel
from apps.orders.models import OrderModel, OrderItemModel
from apps.products.models import ProductModel
from django.db import transaction
from utils.make_woocommerce_request import make_woocommerce_request

def save_order_from_woocommerce(order_data):
    """Saves an order from WooCommerce into the local database.

    This function processes an order received from WooCommerce and stores it in 
    the local database. It ensures data consistency by:
    - Creating or retrieving the associated client.
    - Creating or retrieving the shipping address.
    - Creating the order if it does not already exist.
    - Fetching additional product details from WooCommerce.
    - Associating the products with the order.

    The function operates within a transaction to maintain database integrity. 
    If an error occurs, the transaction is rolled back.

    Args:
        order_data (dict): The order details fetched from WooCommerce, including 
                           client, address, order items, and total.

    Returns:
        OrderModel: The created or retrieved order instance.
        None: If an error occurs during the process.

    Raises:
        Exception: If there is an issue during order processing or database insertion.
    """

    try:
        with transaction.atomic(): 

            client, _ = ClientModel.objects.get_or_create(
                email=order_data["client"]["email"],
                defaults={
                    "name": order_data["client"]["name"],
                    "phone": order_data["client"]["phone"]
                }
            )

            address, _ = AddressModel.objects.get_or_create(
                address=order_data["address"]["address"],
                city=order_data["address"]["city"],
                state=order_data["address"]["state"],
                country=order_data["address"]["country"]
            )

            order, created = OrderModel.objects.get_or_create(
                external_id=order_data["external_id"],
                defaults={
                    "client": client,
                    "address": address,
                    "total": order_data["total"],
                    "status": order_data["status"]
                }
            )

            if not created:
                return order  

            for item in order_data["items"]:
                product_datails = get_product_details(item["product_id"])

                product, _ = ProductModel.objects.get_or_create(
                    id_product=item["product_id"],  
                    defaults={
                        "name": item["name"],
                        "price": item["unit_price"],
                        "inventory": product_datails["inventory"],  
                        "description": product_datails["description"]
                    }
                )

                OrderItemModel.objects.create(
                    order=order,
                    product=product,
                    quantity=item["quantity"],
                    unit_price=item["unit_price"]
                )

            return order 

    except Exception as e:
        print(f"Error al guardar la orden: {e}")
        return None
    
def get_product_details(product_id):

    """Fetches product details from WooCommerce.

    This function retrieves the product's short description and stock quantity 
    from WooCommerce using the product ID.

    Args:
        product_id (int): The ID of the product to fetch details for.

    Returns:
        dict: A dictionary containing:
            - "description" (str): The product's short description.
            - "inventory" (int): The available stock quantity.

    Raises:
        Exception: If an error occurs while fetching the product details.
    """
    try:
        response = make_woocommerce_request(f"products/{product_id}", "GET")
        return {
            "description": response.get("short_description", ""),
            "inventory": response.get("stock_quantity", 0)
        }
    except Exception as e:
        raise Exception(f"Error durante la obtención de los detalles del producto: {e}")
