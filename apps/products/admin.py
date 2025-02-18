from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Register your models here.
@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "id_product", "price", "inventory", "created_at", "updated_at", "preview_image")
    search_fields = ("id_product", "name", "description")
    list_filter = ("created_at", "updated_at", "price")
    ordering = ("id_product",)
    readonly_fields = ("id_product","created_at", "updated_at")
    list_editable = ("price", "inventory")
    list_per_page = 10

    fieldsets = (
        ("Información General", {"fields": ("id_product","name", "description", "image")}),
        ("Inventario y Precio", {"fields": ("price", "inventory")}),
        ("Fechas", {"fields": ("created_at", "updated_at")}),
    )

    actions = ["mark_out_of_stock"]

    def mark_out_of_stock(self, request, queryset):
        """Acción personalizada para marcar productos seleccionados como fuera de stock."""
        queryset.update(inventory=0)
        self.message_user(request, f"{queryset.count()} productos marcados como sin stock.")
    
    def preview_image(self, obj):
        """Muestra una miniatura de la imagen en el admin."""
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:5px"/>', obj.image.url)
        return "Sin imagen"

    mark_out_of_stock.short_description = "Marcar como sin stock"
    preview_image.short_description = "Vista previa"