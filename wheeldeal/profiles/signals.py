from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
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


@receiver(pre_save, sender=UserProfile)
def check_profile_complete(sender, instance: UserProfile, **kwargs):
    if instance.address and \
            instance.first_name and \
            instance.last_name and \
            instance.age and \
            instance.city:

        if not instance.is_deliveryman:
            instance.is_complete = True
            return

        if instance.price_for_delivery and \
                instance.image:
            instance.is_complete = True

