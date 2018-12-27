from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core import settings
from netflix import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
