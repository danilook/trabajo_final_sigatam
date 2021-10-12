from django.forms import *
from .models import Compra,Repuesto


class CompraForm(Form):
     # class Meta:
     #     model = Compra
     #     fields = '__all__'
       cantidad = CharField(widget=TextInput(attrs={'class': 'form-control'}))
       fecha_compra = DateField(widget=DateTimeInput(attrs={'class': 'form-control'}))
       id_repuesto = ModelChoiceField(queryset= Repuesto.objects.all() ,widget=Select(attrs={'class': 'form-control'}))





#
#
# class AltaRepuestoForm(forms.ModelForm):
#     class Meta:
#         model = Repuesto
#         fields = '__all__'
