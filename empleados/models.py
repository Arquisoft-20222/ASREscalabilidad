from django.db import models

CHOISES = (('C.C'), ('T.I'), ('Pasaporte'), ('Otro'))


class Empleados(models.Model):
    name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    num_cell = models.FloatField(null=True, blank=True, default=None)
    email = models.CharField(max_length = 255)
    user = models.CharField(max_length = 255)
    password = models.CharField(max_length = 50)
    entry_date = models.DateTimeField(auto_now_add=True)
    type_document = models.CharField(max_length=6, choices=CHOISES, default='C.C')
    num_document = models.CharField(max_length = 255)    
    birth_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '%s %s %s' % (self.name, self.last_name, self.email, self.user, 
                             self.password, self.type_document, self.num_document)