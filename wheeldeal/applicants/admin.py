from django.contrib import admin

from wheeldeal.applicants.models import Applicant


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    pass