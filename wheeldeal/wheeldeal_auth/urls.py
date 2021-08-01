from django.urls import path

from wheeldeal.wheeldeal_auth.views import register

urlpatterns = [
    path('register/', register, name='register'),
    path('sign-in/', register, name='sign in'),
]