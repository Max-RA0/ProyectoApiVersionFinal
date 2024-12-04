from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ServicioLegalViewSet, DivorcioViewSet, AsesoriaLegalViewSet

router = DefaultRouter()
router.register(r'servicio-legal', ServicioLegalViewSet)
router.register(r'divorcio', DivorcioViewSet)
router.register(r'asesoria-legal', AsesoriaLegalViewSet)

urlpatterns = [
    # Rutas para las vistas tradicionales
    path('home/', views.home, name='home'),  # Página principal
    path('servicios/<str:tipo>/lista_servicios/', views.lista_servicios, name='lista_servicios'),
    path('servicios/<str:tipo>/lista_asesoria/', views.lista_asesoria, name='lista_asesoria'),
    path('servicios/<str:tipo>/crear/', views.crear_servicio, name='crear_servicio'),
    path('servicios/<str:tipo>/editar/<int:pk>/', views.editar_servicio, name='editar_servicio'),
    path('eliminar_servicio/<int:pk>/', views.eliminar_servicio, name='eliminar_servicio'),  
    path('search/', views.search, name='search'),  # Búsqueda de servicios
    # path('<str:tipo>/lista_servicios/', views.lista_servicios, name='lista_servicios'),  # 
    # path('<str:tipo>/lista_asesoria/', views.lista_asesoria, name='lista_asesoria'),  
    # path('<str:tipo>/crear/', views.crear_servicio, name='crear_servicio'),
    # path('<str:tipo>/editar/<int:pk>/', views.editar_servicio, name='editar_servicio'),  

    # Rutas para las API
    path('api/', include(router.urls)),
]
