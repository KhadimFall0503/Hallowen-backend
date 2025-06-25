from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from api.views import CandiesViewSet, DecorationsViewSet

# Crée un seul routeur et enregistre les deux ViewSets dessus
router = DefaultRouter()
router.register('candies', CandiesViewSet, basename='candies')
router.register('decorations', DecorationsViewSet, basename='decorations')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
