from django.urls import path
from .views import crearEmpleado,altaRol,listarEmpleado,editarEmpleado,eliminarEmpleado

urlpatterns = [
  path('crear_empleado/', crearEmpleado, name =  'crear_empleado'),
  path('listar_empleado/', listarEmpleado, name =  'listar_empleado'),
  path('editar_empleado/<int:id_empleado>', editarEmpleado, name = 'editar_empleado' ),
  path('eliminar_empleado/<int:id_empleado>', eliminarEmpleado, name = 'eliminar_empleado' ),
  path('alta_rol/',altaRol, name = 'alta_rol')


]
