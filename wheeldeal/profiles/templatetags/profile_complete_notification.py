from django import template

from wheeldeal.profiles.models import UserProfile

register = template.Library()


@register.inclusion_tag('tags/profile_complete_notification.html', takes_context=True)
def profile_complete_notification(context):
    profile = UserProfile.objects.get(pk=context.request.user.id)
    is_complete = profile.is_complete
    context['is_complete'] = is_complete
    return context
