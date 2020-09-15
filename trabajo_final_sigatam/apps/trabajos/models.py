from django.db import models
import datetime
class Trabajo (models.Model) :
    id_trabajo = models.AutoField (primary_key= True)
    tipo_trabajo = models.CharField ('Tipo de trabajo', max_length= 300 , blank=False, null= False)
    fecha_inicio = models.DateField ('Fecha de inicio' , blank= False, null= False )
    fecha_finalizacion = models.DateField ( 'Fecha de finalizacion', blank= False, null= False)
    detalle = models.CharField ('Detalle de trabajo', max_length= 500, blank=True, null= True)
    estado = models.CharField ('Estadp de trabajo', max_length= 50, blank= False, null= False)
    class Meta:
        verbose_name = 'Trabajo'
        verbose_name_plural = 'Trabajos'
        ordering = ['estado']
    def __str__(self):
        return self.tipo_trabajo

class Presupuesto (models.Model):
    id_presupuesto = models.AutoField (primary_key= True)
    fecha_emision = models.DateField (blank= False, null= False)
    detalles = models.CharField ('Detalles',default= "", max_length= 200 , blank= False, null= False)
    tipo_servicio = models.CharField ('Tipo de servicio' , default= "", max_length= 220, blank= False, null= False)
    Precio = models.IntegerField ('Precio del servicio' , default= 0, blank=False, null= False )
    Observaciones = models.CharField ('Observaciones' , default= "", max_length= 300, blank= False, null= False)
