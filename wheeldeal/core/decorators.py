from django.shortcuts import render

from wheeldeal.core.utils import get_user_profile


def only_delivery_guy_allowed(view_func):
    def wrapper(request, *args, **kwargs):
        userprofile = get_user_profile(request.user.id)
        if not userprofile.is_deliveryman:
            return render(request, 'error_codes/401.html')

        return view_func(request, *args, **kwargs)

    return wrapper
