from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido','dni','direccion','correo','edad']
        labels = {
            'nombre':'Nombre del cliente',
            'apellido': 'Apellido del cliente',
            'dni': ' Dni del cliente',
            'direccion':'Direccion del cliente',
            'Correo': 'Correo Electronico del Cliente',
            'edad': 'Edad del cliente',
        }

        widgets = {

                'nombre': forms.TextInput(
                    attrs ={
                        'class':'form-control',
                        'placeholder':'ingrese nombre del cliente',
                        'id':'nombre'
                    }
                ),
                'apellido': forms.TextInput(
                    attrs = {
                        'class': 'form-control',
                        'placeholder': 'ingrese apellido del cliente',
                        'id': 'apellido'

                    }
                ),
                'dni':forms.NumberInput(
                    attrs = {
                        'class': 'form-control',
                        'placeholder':'ingrese dni del cliente',
                        'id': 'dni'
                    }
                ),
                'direccion':forms.TextInput(
                    attrs = {
                        'class': 'form-control',
                        'placeholder':'ingrese la direccion de residencia del cliente',
                        'id': 'direccion'
                    }
                ),
                'correo':forms.EmailInput(
                    attrs = {
                        'class': 'form-control',
                        'placeholder':'ingrese direccion de email del cliente',
                        'id': 'correo'
                    }
                ),
                'edad':forms.NumberInput(
                    attrs = {
                        'class': 'form-control',
                        'placeholder':'ingrese la edad del cliente',
                        'id': 'edad'
                    }
                ),

        }
