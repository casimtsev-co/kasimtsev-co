from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('admin/', admin.site.urls, name = 'admin'),
   path('account/', include ("users.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
        document_root=settings.STATIC_ROOT)
