from django.db import models

# TODO: Implement the ProductModel

class ProductModel(models.Model):

    id_product = models.AutoField(primary_key=True, verbose_name="ID del Producto")
    name = models.CharField(max_length=255, verbose_name="Nombre")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    inventory = models.PositiveIntegerField(verbose_name="Inventario")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to="products/", blank=True, null=True, verbose_name="Imagen del producto")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name = "Última actualización")

    class Meta:
        ordering = ["id_product"]
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return f"{self.name} - {str(self.price)}"
