from utils.make_woocommerce_request import make_woocommerce_request
from .order_service import save_order_from_woocommerce

def fetch_and_save_orders():
    """Obtiene todas las órdenes de WooCommerce y las guarda en la base de datos."""
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