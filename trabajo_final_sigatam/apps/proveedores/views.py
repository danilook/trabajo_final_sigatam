from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist  # se importa una exeptions #
from .forms import ProveedorForm
from .models import Proveedor,categoria



def crearProveedor(request):                              #Funcion para crear un proveedor #
    if request.method == 'POST':
        proveedor_form = ProveedorForm(request.POST)
        if proveedor_form.is_valid():
            proveedor_form.save()
            return redirect('index')
    else:
        proveedor_form = ProveedorForm()
    return render (request,'proveedores/crear_proveedor.html',{'proveedor_form':proveedor_form})
