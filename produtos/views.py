from django.shortcuts import render
from.models import Produto
from .admin import ProdutoAdmin

def home(request):
    prod = Produto.objects.all()
    prod_list = ProdutoAdmin.list_display
    return render(request, 'home.html', {'prod': prod, 'prod_list': prod_list})
