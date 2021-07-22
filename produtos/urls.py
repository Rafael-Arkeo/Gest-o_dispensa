from django.urls import path
from .views import criar_novo_produto

urlpatterns = [
    path('novo/', criar_novo_produto, name='novo_prod')

]