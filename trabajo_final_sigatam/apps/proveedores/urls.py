from django.urls import path, include
from .views import crearProveedor,listarProveedor,editarProveedor,eliminarProveedor,altaCategoriaProveedor


urlpatterns =[
    path('crear_proveedor/', crearProveedor, name =  'crear_proveedor'),
    path( 'listar_proveedor/', listarProveedor, name = 'listar_proveedor'),
    path( 'editar_proveedor/<int:id_proveedor>', editarProveedor, name = 'editar_proveedor' ),
    path('eliminar_proveedor/<int:id_proveedor>', eliminarProveedor, name = 'eliminar_proveedor' ),
    path( 'alta_categoria_proveedor', altaCategoriaProveedor, name= 'alta_categoria_proveedor')


]
