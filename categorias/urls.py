from django.urls import path
from .views import list_categoria, nova_categoria, nova_categoria_alternativa
from .views import atualizar_categoria, deletar_categoria


urlpatterns = [

    path('list/', list_categoria, name='list-categoria'),
    path('nova', nova_categoria, name='nova-categoria'),
    path('nova2', nova_categoria_alternativa, name='nova-categoria2'),
    path('atualizar/<int:id>/', atualizar_categoria, name='atualizar-categoria'),
    path('deletar/<int:id>/', deletar_categoria, name='deletar-categoria'),
]