from django.db import models


class  Cliente (models.Model):
   id_cliente = models.AutoField (primary_key= True)
   nombre = models.CharField(max_length = 220, blank = False, null = False)
   apellido = models.CharField(max_length = 220, blank = False, null = False)
   dni = models.IntegerField ()
   direccion = models.CharField(max_length = 220, blank = False, null = False)
   correo = models.CharField(max_length = 100, blank = False, null = False)
   edad = models.IntegerField ()
   class Meta:
      verbose_name = 'Cliente'
      verbose_name_plural = 'Clientes'
      ordering = ['nombre']
   def  __str__(self):
      return self.nombre
