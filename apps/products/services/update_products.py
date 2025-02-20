from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from utils.make_woocommerce_request import make_woocommerce_request
from ..models import ProductModel
from ..serializers import ProductSerializer
from rest_framework.exceptions import NotFound

def update_product(request, id_product):

    """Updates a product in WooCommerce and the local database.

    This function first checks if the product exists in WooCommerce. 
    If it does, it updates the corresponding fields. Then, it verifies 
    if the product exists in the local database:
    - If found, it updates the local product details.
    - If not found but successfully updated in WooCommerce, it creates 
      a new local record with the WooCommerce data.

    Args:
        request (Request): The request object containing the update data.
        id_product (int): The ID of the product to be updated.

    Returns:
        dict: The updated product data if successful.
        dict: An error message if the update fails.
    """
    
    data = request.data.copy()
    woocommerce_data = {
        "name": str(data.get("name")),
        "price": str(data.get("price")),
        "stock_quantity": data.get("inventory"),
        "short_description": str(data.get("description")),
    }

    woocommerce_data = {k: v for k, v in woocommerce_data.items() if v is not None}

    woocommerce_updated = False
    woocommerce_product_data = None
    if woocommerce_data:
        response = make_woocommerce_request(f"products/{id_product}", "PATCH", woocommerce_data)
        if 'id' in response:
            woocommerce_updated = True
            woocommerce_product_data = response
        else:
            print(f"Error al actualizar en WooCommerce: {response}")
    try:
        with transaction.atomic():
            try:
                product = ProductModel.objects.get(id_product=id_product)
                serializer = ProductSerializer(product, data=data, partial=True, context={"request": request})
                if serializer.is_valid():
                    serializer.save()
                    return serializer.data
                else:
                    return {"error": serializer.errors}
            except ObjectDoesNotExist:
                if woocommerce_updated and woocommerce_product_data:
                    local_data = {
                        "id_product": woocommerce_product_data["id"],
                        "name": woocommerce_product_data["name"],
                        "price": woocommerce_product_data["regular_price"],
                        "inventory": woocommerce_product_data["stock_quantity"],
                        "description": woocommerce_product_data["short_description"],
                    }
                    serializer = ProductSerializer(data=local_data, context={"request": request})
                    if serializer.is_valid():
                        serializer.save()
                        return serializer.data
                    else:
                        return {"error": serializer.errors}
                else:
                    raise NotFound("Producto no encontrado en la base de datos local y no se pudo actualizar en WooCommerce.")
    except Exception as e:
        print(f"Error al actualizar o crear el producto localmente: {e}")
        return {"error": str(e)}