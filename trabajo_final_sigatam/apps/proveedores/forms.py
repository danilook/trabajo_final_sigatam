from django import forms
from .models import Proveedor,categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = categoria
        fields = '__all__'
        labels = {
            'nombre':'Nombre de la categoria',
        }
        widgets = {
            'nombre':forms.TextInput(
                attrs = {
                 'class':'form-control',
                 'placeholder':'Ingrese el nombre de la categoria',
                 'id': 'nombre'
                }
            )
        }

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        labels = {
            'nombre':'Nombre ',
            'apellido':'Apellido ',
            'dni': 'Dni ',
            'telefono':'Telefono ',
            'correo':'Correo ',
            'direccion':'Direccion ',
            'id_categoria':'Categoria ',

        }
        widgets = {
            'nombre': forms.TextInput(
                attrs ={
                    'class':'form-control',
                    'placeholder':'ingrese nombre del proveedor',
                    'id':'nombre'
                }
            ),
            'apellido': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'ingrese apellido del proveedor',
                    'id': 'apellido'

                }
            ),
            'dni':forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'ingrese dni del proveedor',
                    'id': 'dni'
                }
            ),
            'telefono':forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'ingrese numero telefonico del proveedor',
                    'id': 'telefono'
                }
            ),
            'correo':forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'ingrese direccion de email del proveedor',
                    'id': 'correo'
                }
            ),
            'direccion':forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'ingrese direccion de residencia del proveedor',
                    'id': 'direccion'
                }
            ),
            'id_categoria':forms.Select(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'ingrese numero telefonico del proveedor',
                    'id': 'telefono'
                }
            )









        }
