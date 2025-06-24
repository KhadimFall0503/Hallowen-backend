from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from api.views import CandiesViewSet

# Crée un router pour générer automatiquement les routes CRUD
router = DefaultRouter()
router.register('', CandiesViewSet, basename='candies')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Inclure les routes générées par le router
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
