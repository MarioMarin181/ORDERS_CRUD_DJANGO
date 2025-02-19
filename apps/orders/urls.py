from django.urls import path
from .views import get_orders_woocommerce, get_local_orders, route_index

urlpatterns = [
    path("", route_index),
    path("get_orders_woocommerce/", get_orders_woocommerce, name="get_orders_woocommerce"),
    path("get_local_orders/", get_local_orders, name="get_local_orders"),
]

