from django.urls import path

from wheeldeal.applicants.views import apply

urlpatterns = [
    path('apply/', apply, name='apply'),
]

from .signals import *