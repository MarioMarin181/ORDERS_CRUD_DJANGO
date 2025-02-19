from django.db import models

from apps.clients.models import ClientModel, AddressModel
from apps.products.models import ProductModel

class OrderModel(models.Model):

    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE, verbose_name="Cliente")
    address = models.ForeignKey(AddressModel, on_delete=models.CASCADE, verbose_name="Dirección")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    status = models.CharField(max_length=100, verbose_name="Estatus")
    external_id = models.CharField(max_length=100, unique=True, null=True, verbose_name="ID Externo")

    class Meta:
        ordering = ["id"]
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
    
    def __str__(self):
        return f"{self.client.name} - {self.total} - {self.external_id}"

class OrderItemModel(models.Model):

    quantity = models.IntegerField(verbose_name="Cantidad")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Unitario")
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name="items", verbose_name="Pedido")
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name="Producto")

    class Meta:
        ordering = ["id"]
        verbose_name = "PedidoProducto"
        verbose_name_plural = "PedidosProductos"
    
    def __str__(self):
        return f"{self.quantity} - {self.product.name} - {self.order.external_id}"

    # TODO: Add a foreign key to the ProductModel.