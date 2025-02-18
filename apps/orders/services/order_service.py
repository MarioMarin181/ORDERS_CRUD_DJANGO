from apps.clients.models import ClientModel, AddressModel
from apps.orders.models import OrderModel, OrderItemModel
from apps.products.models import ProductModel
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist

def save_order_from_woocommerce(order_data):
    """Guarda una orden de WooCommerce en la base de datos de manera transaccional."""

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
                product, _ = ProductModel.objects.get_or_create(
                    id_product=item["product_id"],  # ✅ Usamos el `product_id` de WooCommerce
                    defaults={
                        "name": item["name"],
                        "price": item["unit_price"],
                        "inventory": 0,  # ⚠️ Puedes actualizarlo después con el stock real
                        "description": "Producto importado de WooCommerce"
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
        print(f"❌ Error al guardar la orden: {e}")
        return None
