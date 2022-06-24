from django.urls import path
from .views import altaTurno, listarTurno


urlpatterns =[
    path('registrar_turno/', altaTurno, name = 'registrar_turno'),
    path('listar_turno/', listarTurno, name = 'listar_turno')


    ]
