from django import forms
from .models import Empleado,rolEmpleado

class empleadoForm(forms.ModelForm):
    class Meta:
        model= Empleado
        fields = '__all__'
        labels = {
            'nombre':'Nombre del empleado',
            'apellido':'Apellido del empleado',
            'dni': 'Dni del empleado',
            'id_rol':'rol del empleado',
            'fecha_alta':'Fecha de alta del empleado',
            'reputacion':'reputacion del empleado',
        }
        widgets = {
                'nombre': forms.TextInput(
                    attrs ={
                        'class':'form-control',
                        'placeholder':'ingrese nombre del empleado',
                        'id':'nombre'
                    }
                ),
                'apellido': forms.TextInput(
                    attrs = {
                        'class': 'form-control',
                        'placeholder': 'ingrese apellido del empleado',
                        'id': 'apellido'

                    }
                ),
                'dni':forms.NumberInput(
                    attrs = {
                        'class': 'form-control',
                        'placeholder':'ingrese dni del empleado',
                        'id': 'dni'
                    }
                ),
                'id_rol':forms.Select(
                    attrs = {
                        'class': 'form-control',
                        'placeholder':'Seleccione el rol del empleado',
                        'id': 'rol'
                    }
                ),
                'fecha_alta':forms.DateInput(
                    attrs = {
                        'class': 'form-control',
                        'placeholder':'Seleccione la fecha de alta del empleado',
                        'type':'date',
                        'id': 'Fecha'
                    }
                ),
                'reputacion':forms.TextInput(
                    attrs = {
                        'class': 'form-control',
                        'placeholder':'ingrese reputacion del empleado',
                        'id': 'reputacion '
                    }
                )

            }



class rolForm(forms.ModelForm):
    class Meta:
        model= rolEmpleado
        fields= '__all__'
        labels= {
        'nombre':'Nombre del rol',
        }
        widgets= {
            'nombre':forms.TextInput(
                attrs ={
                    'class':'form-control',
                    'placeholder':'ingrese nombre del rol',
                    'id': 'nombre'

                }


            )

        }
