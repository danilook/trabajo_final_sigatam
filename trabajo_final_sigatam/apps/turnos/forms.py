from django import forms
from .models import Turno,tipoTurno

class turnoForm (forms.ModelForm):
    class Meta:
        model = Turno
        fields = '__all__'
        labels = {
            'id_tipoTurno':'Tipo de turno',
            'fecha_turno':'Fecha del turno',
        }
        widgets ={
            'id_tipoTurno':forms.Select(
                attrs ={
                'class': 'form-control',
                'placeholder': 'Seleccione el tipo de turno',
                'id': 'tipo_turno'
                }

            ),
            'fecha_turno':forms.DateTimeInput(
                attrs = {
                  'class':'form-control',
                  'placeholder': 'Seleccione la fecha en que desea su turno',
                  'type':'Date',
                  'id':'fecha_turno'
                }
            )

        }

class tipoTurnoForm (forms.ModelForm):
    class Meta:
        model = tipoTurno
        fields = '__all__'
        labels = {
         'nombre': 'Nombre del tipo de turno',
        }
        widgets = {
         'nombre': forms.TextInput(
            attrs = {
                'class' : 'form-control',
                'placeholder': 'ingrese el nombre del tipo de turno',
                'id':'nombre'
            }
         )
        }
