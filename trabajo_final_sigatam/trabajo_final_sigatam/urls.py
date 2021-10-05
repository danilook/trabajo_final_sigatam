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
from apps.clientes.views import Home
from apps.clientes.views import Login
from apps.proveedores.views import crearProveedor,listarProveedor,eliminarProveedor
urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include(('apps.clientes.urls','Clientes'))),
    path('home/', Home , name = 'index'),
    path('login/',Login, name= 'login'),
    path('proveedores/', include (('apps.proveedores.urls','Proveedores')))
]
