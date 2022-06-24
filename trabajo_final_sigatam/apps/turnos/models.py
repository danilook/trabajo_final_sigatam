from django.db import models

class tipoTurno(models.Model):
    id_tipoTurno = models.AutoField (primary_key=True)
    nombre = models.CharField('Tipo de turno', max_length= 200, blank= False, null=False)
    class meta:
        verbose_name = 'Tipo de turno'
        verbose_name_plural = 'Tipos de turnos'
        ordering = ['nombre']
    def __str__(self):
        return self.nombre


class Turno (models.Model):
    id_turno = models.AutoField (primary_key= True)
    id_tipoTurno = models.ForeignKey (tipoTurno, null= True, on_delete=models.CASCADE)
    fecha_turno = models.DateTimeField('Fecha del turno' , blank= False, null=False, auto_now=False)
    estado = models.BooleanField('Estado', default= True)
    class meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'
        ordering = ['fecha_turno']
