from django.db import models

class Empleados(models.Model):
    name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)


    def __str__(self):
        return '%s %s %s' % (self.name, self.last_name, self.email)