from django.shortcuts import render,redirect
from .forms import empleadoForm


def crearEmpleado(request):                              #Funcion para crear un cliente #
    if request.method == 'POST':
        empleado_form = empleadoForm(request.POST)
        if empleado_form.is_valid():
            empleado_form.save()
            return redirect('index')
    else:
        empleado_form = empleadoForm()
    return render (request,'empleados/crear_empleado.html',{'empleado_form':empleado_form})
