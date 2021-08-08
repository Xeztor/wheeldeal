from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

from wheeldeal.orders.order_states import ORDER_STATES
from wheeldeal.profiles.models import UserProfile

UserModel = get_user_model()


class Order(models.Model):
    PACKAGE_TYPES = [
        ('Small Package', 'Small Package'),
        ('Small Box', 'Small Box'),
        ('medium', 'Medium Box'),
        ('large', 'Large Box'),
    ]

    type = models.CharField(
        choices=PACKAGE_TYPES,
        max_length=30,
    )

    destination_address = models.CharField(
        max_length=100,
    )

    image = models.ImageField(
        upload_to='orders_images',
        blank=True,
    )

    date_made = models.DateTimeField(
        default=datetime.now(),
    )

    date_delivered = models.DateTimeField(
        blank=True,
        null=True,
    )

    state = models.CharField(
        max_length=10,
        default=ORDER_STATES['0']
    )

    client = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='client',
    )

    delivery_guy = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='delivery_guy',
        blank=True,
        null=True,
    )
