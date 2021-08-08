from wheeldeal.profiles.models import UserProfile


def get_user_profile(user_id):
    return UserProfile.objects.get(user_id=user_id)