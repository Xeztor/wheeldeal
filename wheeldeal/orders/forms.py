from django import forms

from wheeldeal.mixins.BootstrapMixins.FormControlMixin import FormControlMixin
from wheeldeal.orders.models import Order


class CreateOrderForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = Order
        fields = ('type', 'destination_address', 'image', )
