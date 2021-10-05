from django.db import models

class categoria (models.Model):
    id_categoria = models.AutoField (primary_key= True)
    nombre = models.CharField(max_length= 200, blank= False, null= False)
    class Meta:
        verbose_name = 'Categoria'   #nombre en singular #
        verbose_name_plural = 'Categorias'  # nombre el plural#
        ordering = ['nombre']     # como queremos de django nos ordene la tabla#
    def __str__(self):
        return self.nombre





class Proveedor (models.Model):
    id_proveedor = models.AutoField (primary_key= True)
    nombre= models.CharField (max_length = 200, blank= False, null= False)
    apellido = models.CharField (max_length = 200, blank= False, null= False)
    dni = models.IntegerField ()
#    categoria = models.CharField (max_length = 250, blank= False, null= False) #
    telefono = models.IntegerField ()
    correo = models.CharField (max_length = 100 , blank= False, null= False)
    direccion = models.CharField (max_length = 250, blank= False, null= False)
    id_categoria = models.ForeignKey (categoria, null= True, on_delete=models.CASCADE)   #relacion entre modelos //proveedor - categoria// #
    estado = models.BooleanField('Estado', default= True)
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['nombre']
    def __str__(self):
        return self.nombre
