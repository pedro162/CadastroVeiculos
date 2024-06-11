
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', listar_carro, name='home'),
    path('cadastrar_carro/', cadastrar_carro, name='cadastrar_carro'),
    path('listar_carro/', listar_carro, name='carro_list'),
    path('editar_carro/<int:pk>', editar_carro, name='editar_carro'),
    path('remover_carro/<int:pk>', remover_carro, name='remover_carro'),
]
