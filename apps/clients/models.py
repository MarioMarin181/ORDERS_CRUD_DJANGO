from django.db import models

class ClientModel(models.Model):

    name = models.CharField(max_length=100, verbose_name="NombreCliente")
    email = models.EmailField(max_length=100, verbose_name="Correo")
    phone = models.CharField(max_length=20, verbose_name="Teléfono")

    class Meta:
        ordering = ["id"]
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    
    def __str__(self):
        return self.name
    
class AddressModel(models.Model):
    
    address = models.CharField(max_length=200, verbose_name="Dirección")
    city = models.CharField(max_length=100, verbose_name="Ciudad")
    state = models.CharField(max_length=100, verbose_name="Estado")
    country = models.CharField(max_length=100, verbose_name="País")

    class Meta:
        ordering = ["id"]
        verbose_name = "Dirección"
        verbose_name_plural = "Direcciones"
    
    def __str__(self):
        return self.address