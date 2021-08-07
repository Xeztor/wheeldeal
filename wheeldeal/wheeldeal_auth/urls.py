from django.urls import path

from wheeldeal.wheeldeal_auth.views import register, login_user, logout_user

urlpatterns = [
    path('register/', register, name='register user'),
    path('login/', login_user, name='login user'),
    path('logout/', logout_user, name='logout user'),
]
