from rest_framework import serializers

from asr_escalabilidad.models import Empleado, Empresa, Pago

class EmpleadoSerializer(serializers.ModelSerializer):
   class Meta:
       model = Empleado
       fields = ('id','name', 'last_name', 'num_cell', 'email', 'user', 'password', 'entry_date', 'type_document', 'num_document', 'birth_date','empresa')
       


class EmpresaSerializer(serializers.ModelSerializer):
   class Meta:
       model = Empresa
       fields = ('id','razon_social', 'nit', 'direccion','empleados', 'pagos')

class PagoSerializer(serializers.ModelSerializer):
   class Meta:
       model = Pago
       fields = ('id','nombre_pago', 'codigo', 'descripcion','fecha_pago','empresa')
