from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist  # se importa una exeptions #
from .forms import empleadoForm,rolForm
from .models import Empleado,rolEmpleado


def crearEmpleado(request):                              #Funcion para crear un empleado #
    if request.method == 'POST':
        empleado_form = empleadoForm(request.POST)
        if empleado_form.is_valid():
                empleado_form.save()
                return redirect('Empleados:listar_empleado')
    else:
        empleado_form = empleadoForm()
    return render (request,'empleados/crear_empleado.html',{'empleado_form':empleado_form})
                                                    #Funcion para dar el alta rol#
def altaRol(request):

    if request.method == 'POST':                                                # se pregunta por el metodo #
        rol_form = rolForm(request.POST)
        if rol_form.is_valid():
             rol_form.save()                                                     # se guardan los cambios en la base de datos#
             return redirect('Empleados:listar_empleado')                        # se redirecciona a la url especificada #
    else:
            rol_form = rolForm()
    roles = rolEmpleado.objects.filter(estado = True)                           # se obtienen los datos de la base de datos    #
    return render (request,'empleados/alta_rol.html',{'rol_form':rol_form,'roles':roles})   # se envia la variable al template#


def listarEmpleado(request):
    empleados = Empleado.objects.filter(estado = True) #variable empleados trae los datos de la base de datos #
    return render (request,'empleados/listar_empleado.html',{'empleados': empleados})   # se envia la variable al template#



def editarEmpleado(request,id_empleado):                              #funcion para editar un proveedores#
    empleado_form = None
    error = None
    try:
        empleado = Empleado.objects.get(id_empleado = id_empleado)
        if request.method == 'GET' :
            empleado_form = empleadoForm (instance= empleado)
        else:
            empleado_form = empleadoForm (request.POST, instance = empleado)
            if empleado_form.is_valid():
                empleado_form.save()
            return  redirect('index')
    except   ObjectDoesNotExist  as e:
      error = e

    return render(request,'empleados/crear_empleado.html',{'empleado_form': empleado_form, 'error':error})


def eliminarEmpleado(request,id_empleado):
    empleados = Empleado.objects.get(id_empleado = id_empleado)
    if request.method == 'POST' :
        empleados.estado = False
        empleados.save()
        return redirect ('Empleados:listar_empleado')
    return render (request,'Empleados/eliminar_empleado.html',{'empleados':empleados})
