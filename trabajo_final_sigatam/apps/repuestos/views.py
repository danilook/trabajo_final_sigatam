from django.views.generic import TemplateView
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .forms import CompraForm , AltaRepuestoForm
from .models import Repuesto

def altaCompra (request):
     if request.method == 'POST':
         compra_form = CompraForm(request.POST)
         if compra_form.is_valid():
             compra_form.save()
             return redirect ('index')
     else:
        compra_form= CompraForm()

     return render (request, 'repuestos/alta_compra.html',{'compra_form': compra_form})

def altaRepuesto (request):
    if request.method == 'POST':
        alta_form = AltaRepuestoForm(request.POST)
        if alta_form.is_valid():
            alta_form.save()
            return redirect ('Repuestos:registrar_compra')
    else:
        alta_form= AltaRepuestoForm()
    return render (request,'repuestos/modalrepuestos.html',{'alta_form':alta_form})

def editarRepuesto(request,id_repuesto):                              #funcion para editar un proveedores#
    repuesto_form = None
    error = None
    try:
        repuesto = Repuesto.objects.get(id_repuesto = id_repuesto)
        if request.method == 'GET' :
            repuesto_form = AltaRepuestoForm (instance= repuesto)
        else:
            repuesto_form = AltaRepuestoForm (request.POST, instance = repuesto)
            if repuesto_form.is_valid():
                repuesto_form.save()
            return  redirect('index')
    except   ObjectDoesNotExist  as e:
      error = e

    return render(request,'repuestos/registrar_repuesto.html',{'repuesto_form': repuesto_form, 'error':error})


def listarRepuesto(request):
    repuestos = Repuesto.objects.filter(estado = True)
    return render (request,'repuestos/listar_repuesto.html',{'repuestos': repuestos})
