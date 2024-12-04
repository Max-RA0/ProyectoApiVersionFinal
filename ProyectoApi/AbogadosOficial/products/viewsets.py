from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AsesoriaLegalSet, DivorcioSet, ServicioLegalViewSet

router = DefaultRouter()
router.register(r'asesoria-legal', AsesoriaLegalSet)
router.register(r'divorcio', DivorcioSet)
router.register(r'servicio-legal', ServicioLegalViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Página principal
]
