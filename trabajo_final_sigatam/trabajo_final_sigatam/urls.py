"""trabajo_final_sigatam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.decorators import login_required  #importamos la clase propia de django para manejar login #
from apps.clientes.views import Home
from apps.proveedores.views import crearProveedor,listarProveedor,eliminarProveedor,altaCategoriaProveedor
from apps.usuario.views import Login,logoutUsuario
from apps.repuestos.views import altaCompra, altaRepuesto
from apps.empleados.views import crearEmpleado
urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include(('apps.clientes.urls','Clientes'))),
    path('home/', Home , name = 'index'),
    path('proveedores/', include (('apps.proveedores.urls','Proveedores'))),
    path('accounts/login/',Login.as_view(), name = 'login'),
    path('logout/',login_required(logoutUsuario),name = 'logout'),
    path('repuestos/', include(('apps.repuestos.urls','Repuestos'))),
    path('empleados/', include(('apps.empleados.urls','Empleados'))),


]
