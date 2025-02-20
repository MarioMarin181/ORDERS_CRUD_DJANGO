from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ClientModel)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email","phone")
    search_fields = ("id", "name", "email")
    ordering = ("id",)
    readonly_fields = ("id",)

@admin.register(AddressModel)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("id", "address", "city", "state", "country")
    search_fields = ("id", "address", "city", "state", "country")
    list_filter = ("city", "state", "country")
    ordering = ("id",)
    readonly_fields = ("id",)