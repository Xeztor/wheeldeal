from django.urls import path

from .views import profile_details, profile_edit

urlpatterns = [
    path('details/', profile_details, name='profile details'),
    path('edit/', profile_edit, name='profile edit'),
]

from .signals import *
