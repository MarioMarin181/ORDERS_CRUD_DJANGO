from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "get_client_id","get_client_name", "total", "status", "created_at", "status", "external_id")
    search_fields = ("id", "client__name", "external_id")
    list_filter = ("status", "created_at")
    ordering = ("id",)
    readonly_fields = ("id", "created_at")

    def get_client_name(self, obj):
        return obj.client.name
    
    def get_client_id(self, obj):
        return obj.client.id
    
    get_client_name.short_description = "Nombre del Cliente"
    get_client_id.short_descripction = "Id del Cliente"

@admin.register(OrderItemModel)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "product", "quantity", "unit_price")
    search_fields = ("id", "order__external_id", "product__name")
    list_filter = ("order", "product")
    ordering = ["order"]

