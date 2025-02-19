from utils.make_woocommerce_request import make_woocommerce_request
from .order_service import save_order_from_woocommerce

def fetch_and_save_orders():
    """Fetches orders from WooCommerce and saves them in the local database.

    This function retrieves all orders from WooCommerce and processes them to:
    - Extract relevant order details such as client information, address, 
      order items, and total amount.
    - Transform the data to match the local database schema.
    - Save each order in the local database using `save_order_from_woocommerce`.
    - Track successfully saved orders.

    If an error occurs during the process, an exception is raised.

    Returns:
        dict: A dictionary containing:
            - "id_ordenes_guardadas" (list): A list of successfully saved order IDs.

    Raises:
        Exception: If an error occurs while fetching or processing orders.
    """
    
    try:
        orders = make_woocommerce_request("orders", "GET")
        saved_orders = []
        for order in orders:
            order_data = {
                "external_id": order["id"],
                "total": order["total"],
                "status": order["status"],
                "client": {
                    "name": f"{order['billing']['first_name']} {order['billing']['last_name']}",
                    "email": order["billing"]["email"],
                    "phone": order["billing"]["phone"]
                },
                "address": {
                    "address": order["billing"]["address_1"],
                    "city": order["billing"]["city"],
                    "state": order["billing"]["state"],
                    "country": order["billing"]["country"]
                },
                "items": [
                    {
                        "name": item["name"],
                        "product_id": item["product_id"],
                        "quantity": item["quantity"],
                        "unit_price": item["price"]
                    } for item in order["line_items"]
                ]
            }
            saved_order = save_order_from_woocommerce(order_data)
            if saved_order:
                saved_orders.append(saved_order.external_id)
        return {"id_ordenes_guardadas": saved_orders}
    except Exception as e:
        raise Exception(f"Error durante la obtención de los pedidos en woocommerce: {e}")