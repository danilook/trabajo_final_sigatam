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

class Faltante (models.Model)  :
    id_faltante = models.AutoField (primary_key = True)
    faltante = models.CharField ('faltante', max_length = 200, blank = False, null = False)
    class Meta:
        verbose_name = 'Faltente'
        verbose_name_plural = 'Faltantes'
        ordering = ['faltante']
        def __str__ (self):
            return self.faltante

class Compra (models.Model) :
    id_compra = models.AutoField (primary_key = True)
    cantidad= models.CharField ('cantidad', max_length= 200, blank= False , null = False )
    fecha_compra= models.DateField  ('fecha compra ', blank= False, null= False )

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        ordering = ['cantidad']
    def __str__ (self) :
        return self.cantidad
