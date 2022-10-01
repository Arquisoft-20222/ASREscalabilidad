from django.urls import include, path

from rest_framework import routers

from asr_escalabilidad.views import EmpleadoViewSet, EmpresaViewSet

router = routers.DefaultRouter()
router.register(r'empleados', EmpleadoViewSet)
router.register(r'empresas', EmpresaViewSet)

urlpatterns = [
   path('', include(router.urls)),
]