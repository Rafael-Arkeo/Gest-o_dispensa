from django.shortcuts import render, redirect
from.models import Produto
from .admin import ProdutoAdmin
from .forms import ProdForms

def home(request):
    prod = Produto.objects.all()
    index = ProdutoAdmin.list_display
    return render(request, 'home.html', {'prod': prod, 'index': index})


def criar_novo_produto(request):
    form = ProdForms(request.POST, None)
    """"Cria formulário para cadastrar
            um novo produto"""
    if form.is_valid():
        """"Valida o cadastro"""
        form.save()
        return redirect('home')
        """"Retorna para página home"""
    return render(request, 'novo_produto.html', {'form': form})
    """"Chama o template novo_produto"""