from django.urls import path
from .views import get_local_clients, get_local_address, route_index

urlpatterns = [
    path("", route_index),
    path("get_local_address/", get_local_address, name="get_local_address"),
    path("get_local_clients/", get_local_clients, name="get_local_clients"),
]

