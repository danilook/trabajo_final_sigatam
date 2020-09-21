from django.urls import path
from .views import crearCliente


urlpatterns =[
    path('crear_cliente/', crearCliente, name =  'crear_cliente')
]
