from django.urls import path

from wheeldeal.common.views import index

urlpatterns = [
    path('', index, name='index'),
]