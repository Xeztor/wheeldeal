from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from wheeldeal import settings

media = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wheeldeal.common.urls')),
    path('', include('wheeldeal.wheeldeal_auth.urls')),
    path('profiles/', include('wheeldeal.profiles.urls')),
    path('orders/', include('wheeldeal.orders.urls')),
] + media
