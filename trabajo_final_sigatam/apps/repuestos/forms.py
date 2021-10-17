
from django import forms
from .models import Compra,Repuesto
from apps.proveedores.models import categoria

class CompraForm(forms.ModelForm):
     class Meta:
         model = Compra
         fields = '__all__'
       # model = Compra
       # cantidad = CharField(widget=TextInput(attrs={'class': 'form-control'}))
       # fecha_compra = DateField(widget=DateTimeInput(attrs={'class': 'form-control'}))








class AltaRepuestoForm(forms.ModelForm):
    class Meta:
        model = Repuesto
        fields = '__all__'
