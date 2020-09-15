from django.db import models
import datetime


class Empleado(models.Model):
  id_empleado = models.AutoField (primary_key = True)
  nombre = models.CharField (max_length = 200, blank = False, null = False)
  apellido = models.CharField ( max_length = 250, blank = False, null = False)
  dni = models.IntegerField ()
  rol = models.CharField (max_length = 200 , blank = False, null = False)
  fecha_alta = models.DateField(blank = False, null = False)
  reputacion = models.IntegerField ()
  class meta:
    verbose_name = 'Empleado'
    verbose_name_plural = 'Empleados'
    ordering = ['nombre']
  def __str__(self):
    return self.nombre 
