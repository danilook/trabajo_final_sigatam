from django.shortcuts import render
from .forms import ClienteForm
from .models import Cliente
def Home(request):
    return render (request,'index.html')

def crearCliente(request):                              #Funcion para crear un cliente #
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect('index')
    else:
        cliente_form = ClienteForm()
    return render (request,'clientes/crear_cliente.html',{'cliente_form':cliente_form})

def listarCliente(request):                                #funcion para listar un cliente #
    clientes = Cliente.objects.all()                   #traemos todos los clientes registrados en la base de datos#
    return render(request,'clientes/listar_cliente.html',{'clientes':clientes})   #retornamos para renderizar en un template#
