from django.urls import path
from .views import get_products_database, product_partial_update

urlpatterns = [
    path("get_products_database/", get_products_database, name="get_products_databse"),
    path("product_partial_update/<int:id_product>/", product_partial_update, name="product_partial_update")
]