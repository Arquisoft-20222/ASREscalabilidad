from rest_framework import viewsets

from asr_escalabilidad.serializers import EmpleadoSerializer, EmpresaSerializer, PagoSerializer
from asr_escalabilidad.models import Empleado, Empresa, Pago


class EmpleadoViewSet(viewsets.ModelViewSet):
   queryset = Empleado.objects.all()
   serializer_class = EmpleadoSerializer


class EmpresaViewSet(viewsets.ModelViewSet):
   queryset = Empresa.objects.all()
   serializer_class = EmpresaSerializer

class PagoViewSet(viewsets.ModelViewSet):
   queryset = Pago.objects.all()
   serializer_class = PagoSerializer