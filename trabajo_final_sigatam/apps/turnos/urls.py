from django.urls import path
from .views import altaTurno


urlpatterns =[
    path('registrar_turno/', altaTurno, name = 'registrar_turno')


    ]
