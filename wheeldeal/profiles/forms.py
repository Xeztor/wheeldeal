from django import forms

from wheeldeal.mixins.BootstrapMixins.FormControlMixin import FormControlMixin
from wheeldeal.profiles.models import UserProfile


class ClientProfileForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'image', 'address', 'age', 'city', ]


class DeliveryManProfileForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['is_deliveryman', 'is_client', 'is_complete', 'user', ]
