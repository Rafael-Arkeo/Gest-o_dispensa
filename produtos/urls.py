from django.urls import path
from .views import criar_novo_produto, deletar_produto
from .views import atualizar_produto


urlpatterns = [
    path('novo/', criar_novo_produto, name='novo_prod'),
    path('deletar/<int:id>/', deletar_produto, name='del'),
    path('update/<int:id>/', atualizar_produto, name='atualizar'),

]