from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from wheeldeal.wheeldeal_auth.managers import WheelDealUserManager


class WheelDealUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = 'email'

    objects = WheelDealUserManager()

