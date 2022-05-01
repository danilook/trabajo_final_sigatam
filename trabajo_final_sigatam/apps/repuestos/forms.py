
from django import forms
from .models import Compra,Repuesto
from apps.proveedores.models import categoria, Proveedor

class CompraForm(forms.ModelForm):
     class Meta:
         model = Compra
         fields = '__all__'

         widgets = {
             'fecha_compra' : forms.DateInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'Seleccione fecha de compra',
                    'type':'date',
                    'id':'fecha_compra'

                }
             ),
             'cantidad': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Seleccione la cantidad de repuestos',
                    'id':'cantidad'


                }
             ),
             'id_repuesto': forms.Select(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Seleccione un repuesto',
                    'id': 'repuesto'

                }
            ),
             'id_proveedor': forms.Select(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'Seleccione proveedor al cual se realizo la compra',
                    'id':'proveedor'
                }
             )
          }

class AltaRepuestoForm(forms.ModelForm):
    class Meta:
        model = Repuesto
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese nombre del repuesto',
                    'id': 'repuesto'
                }
            ),
            'stock': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'ingrese stock',
                    'id': 'stock'

                }
            ),
            'id_categoria':forms.Select(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'Seleccione la categoria del este repuesto',
                    'id':'categoria'
                }
            )








        }
