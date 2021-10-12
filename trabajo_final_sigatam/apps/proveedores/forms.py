from django import forms
from .models import Proveedor,categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = categoria
        fields = '__all__'

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
