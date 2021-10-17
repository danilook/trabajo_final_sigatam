from django.urls import path , include
from apps.proveedores.views import crearProveedor,listarProveedor,eliminarProveedor,altaCategoriaProveedor
from apps.repuestos.views import altaCompra, altaRepuesto



urlpatterns =[
    path('registrar_compra/', altaCompra, name = 'registrar_compra'),
    path('registrar_repuesto/', altaRepuesto, name = 'registrar_repuesto'),
    path('proveedores/', include (('apps.proveedores.urls','Proveedores')))

    ]
