from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('', include('glowny.urls')),
                  path('items/', include('przedmioty.urls')),
                  path('dashboard/', include('panel.urls')),
                  path('admin/', admin.site.urls),
                  path('konto/', include('konto.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)