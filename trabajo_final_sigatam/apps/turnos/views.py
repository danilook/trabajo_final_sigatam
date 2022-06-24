from django.shortcuts import render, redirect
from .forms import  turnoForm
from .models import tipoTurno, Turno

# FUNCION PARA DAR DE ALTA UN TURNO #
def altaTurno (request):
     if request.method == 'POST':                   # PREGUNTAMOS POR EL METODO#
         turno_form = turnoForm(request.POST)       # CREAMOS VARIABLE TURNO_FORM #
         if turno_form.is_valid():                  # PREGUNTAMOS SI ES VALIDO EL FORMULARIO #
             turno_form.save()                      # MIGRAMOS A LA BASE DE DATOS #
             return redirect ('index')              # REDIRECT A DIRECCION URL DESEADA #
     else:                                          # SI NO #
         turno_form = turnoForm()                   # CREAMOS VARIABLE TURNO_FORM #
     return render (request, 'turnos/crear_turno.html',{'turno_form': turno_form})  # RENDERIZAMOS EL TEMPLATE CREAR TURNO Y LE PASAMOS EL FORMULARIO #


# FUNCION PARA LISTAR TURNOS  #
def listarTurno (request):
    turnos = Turno.objects.filter(estado = True)                           #  FILTRAMOS LOS OBJETOS POR ESTADO
    return render (request,'turnos/listar_turno.html',{'turnos': turnos})  # RENDERIZAMOS EL TEMPLATE 
