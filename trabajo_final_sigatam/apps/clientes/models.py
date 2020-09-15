from django.db import models


class  Cliente (models.Model):
   id_cliente = models.AutoField (primary_key= True)
   nombre = models.CharField(max_length = 220, blank = False, null = False)
   apellido = models.CharField(max_length = 220, blank = False, null = False)
   dni = models.IntegerField ()
   direccion = models.CharField(max_length = 220, blank = False, null = False)
   correo = models.CharField(max_length = 100, blank = False, null = False)
   edad = models.IntegerField ()
   
