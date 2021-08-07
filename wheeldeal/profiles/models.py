from django.contrib.auth import get_user_model
from django.db import models

from wheeldeal.common.models import City

UserModel = get_user_model()


class UserProfile(models.Model):
    is_complete = models.BooleanField(
        default=False,
    )

    first_name = models.CharField(
        max_length=20,
    )

    last_name = models.CharField(
        max_length=20,
    )

    image = models.ImageField(
        upload_to='profile_images',
    )

    is_client = models.BooleanField(
        default=True,
    )

    is_deliveryman = models.BooleanField(
        default=False,
    )

    address = models.CharField(
        max_length=50,
    )

    age = models.IntegerField(
        null=True,
    )

    price_for_delivery = models.DecimalField(
        decimal_places=2,
        max_digits=4,
        null=True,
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        null=True,
    )


    user = models.OneToOneField(
        UserModel,
        primary_key=True,
        on_delete=models.CASCADE,
    )
