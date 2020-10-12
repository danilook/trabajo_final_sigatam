from django.urls import path
from .views import crearCliente,listarCliente,editarCliente


urlpatterns =[
    path('crear_cliente/', crearCliente, name =  'crear_cliente'),
    path('listar_cliente/', listarCliente, name= 'listar_cliente'),
    path('editar_cliente/<int:dni>',editarCliente, name= 'editar_cliente')
]
