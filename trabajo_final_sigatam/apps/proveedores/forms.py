from django import forms
from .models import Proveedor,categoria

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'apellido','dni','telefono', 'correo', 'direccion']
