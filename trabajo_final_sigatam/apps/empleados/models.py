from django.db import models
import datetime

class rolEmpleado(models.Model):
    id_rol= models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 200, blank = False, null= False)
    estado = models.BooleanField('Estado', default= True)
    class meta:
        verbose_name = 'rol empleado'
        verbose_name_plural= 'rol empleados'
        ordering=['nombre']
    def __str__(self):
        return self.nombre




class Empleado(models.Model):
  id_empleado = models.AutoField (primary_key = True)
  nombre = models.CharField (max_length = 200, blank = False, null = False)
  apellido = models.CharField ( max_length = 250, blank = False, null = False)
  dni = models.IntegerField ()
  id_rol = models.ForeignKey (rolEmpleado, null= True, on_delete=models.CASCADE)
  fecha_alta = models.DateField(blank = False, null = False)
  reputacion = models.IntegerField ()
  estado = models.BooleanField('Estado', default= True)
  class meta:
    verbose_name = 'Empleado'
    verbose_name_plural = 'Empleados'
    ordering = ['nombre']
  def __str__(self):
    return self.nombre
