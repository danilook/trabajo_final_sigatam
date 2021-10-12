from django.urls import path , include
from apps.proveedores.views import crearProveedor,listarProveedor,eliminarProveedor,altaCategoriaProveedor
from .apps.repuestos.views import altaCompraView



urlpatterns =[
    path('registrar_compra/', altaCompraView.as_views(), name = 'registrar_compra'),
    path('registrar_repuesto', altaRepuesto, name = 'registrar_repuesto'),
    path('proveedores/', include (('apps.proveedores.urls','Proveedores')))

    ]
