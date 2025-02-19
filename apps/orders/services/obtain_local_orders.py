from ..models import OrderModel
from ..serializers import OrderSerializer

def obtain_local_orders():

    orders = OrderModel.objects.all()
    serialized_orders = OrderSerializer(orders, many = True)
    return serialized_orders.data