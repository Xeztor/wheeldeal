from django.db.models.signals import pre_save
from django.dispatch import receiver

from wheeldeal.applicants.models import Applicant
from wheeldeal.profiles.models import UserProfile


@receiver(pre_save, sender=Applicant)
def is_applicant_approved(sender, instance: Applicant, **kwargs):
    if instance.is_approved:
        user = instance.user
        profile = UserProfile.objects.get(pk=user.id)
        profile.is_deliveryman = True
        profile.save()
