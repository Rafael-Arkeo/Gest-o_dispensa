from django.urls import path
from .views import list_categoria, nova_categoria


urlpatterns = [

    path('list/', list_categoria, name='list-categoria'),
    path('nova', nova_categoria, name='nova-categoria'),
]