from django.contrib import admin

from wheeldeal.profiles.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', )
    readonly_fields = ('user', )
