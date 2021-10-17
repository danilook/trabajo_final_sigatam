from django.urls import path
from .views import crearEmpleado

urlpatterns = [
  path('crear_empleado/', crearEmpleado, name =  'crear_empleado')

]
