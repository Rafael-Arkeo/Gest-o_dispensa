from django.shortcuts import render
from.models import Produto
from .admin import ProdutoAdmin

def home(request):
    prod = Produto.objects.all()
    index = ProdutoAdmin.list_display
    return render(request, 'home.html', {'prod': prod, 'index': index})
