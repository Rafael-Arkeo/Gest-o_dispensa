from django.shortcuts import render, redirect, get_object_or_404
from.models import Produto
from .admin import ProdutoAdmin
from .forms import ProdForms

def home(request):
    prod = Produto.objects.all()
    index = ProdutoAdmin.list_display
    return render(request, 'home.html', {'prod': prod, 'index': index})


def criar_novo_produto(request):
    form = ProdForms(request.POST or None)
    """"Cria formulário para cadastrar
            um novo produto"""
    if form.is_valid():
        """"Valida o cadastro"""
        form.save()
        return redirect('home')
        """"Retorna para página home"""
    return render(request, 'novo_produto.html', {'form': form})
    """"Chama o template novo_produto"""


def deletar_produto(request,id):
    prod = get_object_or_404(Produto, pk=id)
    form = ProdForms(request.POST or None, instance=prod)
    if request.method == 'POST':
        prod.delete()
        return redirect('home')
    return render(request, 'deletar_produto.html', {'prod': prod})


def atualizar_produto(request, id):
    prod = get_object_or_404(Produto, pk=id)
    form = ProdForms(request.POST or None, instance=prod)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'atualizar_produto.html', {'form': form})