from django.contrib import admin

from wheeldeal.common.models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', )
    ordering = ('name', )

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name
