from django.db import models

class Repuesto (models.Model) :
    id_repuesto = models.AutoField (primary_key= True)
    nombre = models.CharField ('nombre',max_length= 200, blank= False, null= False)
    stock = models.IntegerField(default= 0 )
    categoria = models.CharField ('categoria', max_length= 200, blank= False, null= False)
    class Meta:
       verbose_name = 'Repuesto'
       verbose_name_plural = 'Repuestos'
       ordering = ['nombre']
    def __str__ (self):
       return self.nombre
