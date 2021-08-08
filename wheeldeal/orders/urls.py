from django.urls import path

from wheeldeal.orders.views import add_order, orders_available, take_order, order_details, orders_history, \
    complete_order

urlpatterns = [
    path('history/', orders_history, name='orders history'),
    path('available/', orders_available, name='orders available'),
    path('add/', add_order, name='add order'),
    path('order_details/<int:pk>', order_details, name='order details'),
    path('take_order/<int:pk>', take_order, name='take order'),
    path('complete_order/<int:pk>', complete_order, name='complete order')
]
