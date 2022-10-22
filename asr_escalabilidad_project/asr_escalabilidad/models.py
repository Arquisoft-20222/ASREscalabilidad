from django.db import models

# Create your models here.


class Empresa(models.Model):
    razon_social = models.CharField(max_length=255)
    nit = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)

class Empleado(models.Model):

    name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    num_cell = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    user = models.CharField(max_length = 255)
    password = models.CharField(max_length = 50)
    entry_date = models.DateTimeField(auto_now_add=True)
    type_document = models.CharField(max_length = 50)
    num_document = models.CharField(max_length = 255)    
    birth_date = models.DateTimeField(auto_now_add=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING, related_name='empleados')

class Pago(models.Model):
    nombre_pago = models.CharField(max_length = 255)
    codigo = models.CharField(max_length = 255)
    descripcion = models.CharField(max_length = 255)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING, related_name='pagos')
