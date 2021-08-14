from django.urls import path

from wheeldeal.orders.views import add_order, orders_available, take_order, order_details, orders_history, \
    complete_order, order_edit, order_delete

urlpatterns = [
    path('history/', orders_history, name='orders history'),
    path('available/', orders_available, name='orders available'),
    path('add/', add_order, name='add order'),
    path('edit/<int:pk>', order_edit, name='order edit'),
    path('delete/<int:pk>', order_delete, name='order delete'),
    path('order_details/<int:pk>', order_details, name='order details'),
    path('take_order/<int:pk>', take_order, name='take order'),
    path('complete_order/<int:pk>', complete_order, name='complete order'),
]
