from django.shortcuts import render

from wheeldeal.profiles.models import UserProfile


def index(request):
    context = {}
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user_id=request.user.id)
        context['is_complete'] = profile.is_complete,

    return render(request, 'common/index.html', context)
