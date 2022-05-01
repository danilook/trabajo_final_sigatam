from django.shortcuts import render, redirect
from .forms import  turnoForm
from .models import tipoTurno, Turno

def altaTurno (request):
     if request.method == 'POST':
         turno_form = turnoForm(request.POST)
         if turno_form.is_valid():
             turno_form.save()
             return redirect ('index')
     else:
         turno_form = turnoForm()
     return render (request, 'turnos/crear_turno.html',{'turno_form': turno_form})
