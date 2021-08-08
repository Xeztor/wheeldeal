from django.contrib import admin

from wheeldeal.orders.models import Order


@admin.display(description='orderid')
def display_order_id(obj):
    return f"OrderID #{obj.id}"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (display_order_id, 'state', )
    ordering = ('id',)
