from django.db import models


class Turno (models.Model):
    id_turno = models.AutoField (primary_key= True)
    tipo_turno = models.CharField ('Tipo de turno' , max_length= 200 , blank= False, null= False)
    fecha_turno = models.DateField('Fecha del turno' , blank= False, null=False)
    class meta:
        verbose_name = 'Turno'
        verbose_name_plurak = 'Turnos'
        ordering = ['fecha_turno']
    def __str__(self):
        return self.tipo_turno
