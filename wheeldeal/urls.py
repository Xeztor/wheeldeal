from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from wheeldeal import settings

media = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),
] + media
