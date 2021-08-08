from django.urls import path

from wheeldeal.common.views import IndexView, AboutUsView, ContactsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about-us/', AboutUsView.as_view(), name='about us'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
]