from django.urls import path
from .views import crearProveedor


urlpatterns =[
    path('crear_proveedor/', crearProveedor, name =  'crear_proveedor'),



]
