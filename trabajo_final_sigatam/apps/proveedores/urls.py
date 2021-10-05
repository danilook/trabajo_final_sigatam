from django.urls import path
from .views import crearProveedor,listarProveedor,editarProveedor,eliminarProveedor


urlpatterns =[
    path('crear_proveedor/', crearProveedor, name =  'crear_proveedor'),
    path( 'listar_proveedor/', listarProveedor, name = 'listar_proveedor'),
    path( 'editar_proveedor/<int:id_proveedor>', editarProveedor, name = 'editar_proveedor' ),
    path('eliminar_proveedor/<int:id_proveedor>', eliminarProveedor, name = 'eliminar_proveedor' )



]
