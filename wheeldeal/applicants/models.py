from django.contrib.auth import get_user_model
from django.db import models

from wheeldeal.wheeldeal_auth.models import WheelDealUser

UserModel = get_user_model()


class Applicant(models.Model):
    front_side_id_image = models.ImageField(
        upload_to='applicants',
    )
    back_side_id_image = models.ImageField(
        upload_to='applicants',
    )
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
    )
    is_approved = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f"{self.user.email}"
