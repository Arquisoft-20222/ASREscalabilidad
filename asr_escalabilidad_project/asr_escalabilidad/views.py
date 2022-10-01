from rest_framework import viewsets

from asr_escalabilidad.serializers import EmpleadoSerializer, EmpresaSerializer
from asr_escalabilidad.models import Empleado, Empresa


class EmpleadoViewSet(viewsets.ModelViewSet):
   queryset = Empleado.objects.all()
   serializer_class = EmpleadoSerializer


class EmpresaViewSet(viewsets.ModelViewSet):
   queryset = Empresa.objects.all()
   serializer_class = EmpresaSerializer