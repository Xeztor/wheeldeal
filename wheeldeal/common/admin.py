from django.contrib import admin

from wheeldeal.common.models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', )
    ordering = ('name', )

