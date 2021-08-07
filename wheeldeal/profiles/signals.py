from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from wheeldeal.profiles.models import UserProfile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile(
            user=instance,
        )
        profile.save()
