from django import template

from wheeldeal.core.utils import get_user_profile
from wheeldeal.profiles.models import UserProfile

register = template.Library()


@register.inclusion_tag('tags/blank.html', takes_context=True)
def add_profile_context(context):
    profile = get_user_profile(context.request.user.id)
    context['profile'] = profile
    return context


@register.inclusion_tag('tags/profile_complete_notification.html', takes_context=True)
def profile_complete_notification(context):
    profile = get_user_profile(context.request.user.id)
    context['is_complete'] = profile.is_complete
    return context


@register.inclusion_tag('tags/profile_image.html', takes_context=True)
def profile_image(context, height):
    profile = get_user_profile(context.request.user.id)
    context['profile_image'] = profile.image
    context['profile_image_height'] = height
    return context
