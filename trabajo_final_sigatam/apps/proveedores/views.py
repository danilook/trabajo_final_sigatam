from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist  # se importa una exeptions #
from .forms import ProveedorForm, CategoriaForm
from .models import Proveedor,categoria

def altaCategoriaProveedor(request):
    if request.method == 'POST':
        categoria_form = CategoriaForm(request.POST)
        if categoria_form.is_valid():
            categoria_form.save()
            return redirect ('index')
    else:
        categoria_form = CategoriaForm()

    return render (request, 'proveedores/alta_categoria_proveedor.html',{'categoria_form': categoria_form})

def crearProveedor(request):                              #Funcion para crear un proveedor #
    if request.method == 'POST':
        proveedor_form = ProveedorForm(request.POST)
        if proveedor_form.is_valid():
            proveedor_form.save()
            return redirect('Proveedores:listar_proveedor')
    else:
        proveedor_form = ProveedorForm()
    return render (request,'proveedores/crear_proveedor.html',{'proveedor_form': proveedor_form})

def listarProveedor(request):
    proveedores = Proveedor.objects.filter(estado = True)
    return render (request,'proveedores/listar_proveedor.html',{'proveedores': proveedores})

def editarProveedor(request,id_proveedor):                              #funcion para editar un proveedores#
    proveedor_form = None
    error = None
    try:
        proveedor = Proveedor.objects.get(id_proveedor = id_proveedor)
        if request.method == 'GET' :
            proveedor_form = ProveedorForm (instance= proveedor)
        else:
            proveedor_form = ProveedorForm (request.POST, instance = proveedor)
            if proveedor_form.is_valid():
                proveedor_form.save()
            return  redirect('index')
    except   ObjectDoesNotExist  as e:
      error = e

    return render(request,'proveedores/crear_proveedor.html',{'proveedor_form': proveedor_form, 'error':error})

def eliminarProveedor(request,id_proveedor):
        proveedor = Proveedor.objects.get(id_proveedor = id_proveedor)
        if request.method == 'POST' :
            proveedor.estado = False
            proveedor.save()
            return redirect ('Proveedores:listar_proveedor')
        return render (request,'Proveedores/eliminar_proveedor.html',{'proveedor':proveedor})
