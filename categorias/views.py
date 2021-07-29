from django.shortcuts import render, redirect
from produtos.models import Categoria
from .forms import CategoriaForm


def list_categoria(request):
    cat = Categoria.objects.all()
    return render(request, 'lista-categoria.html', {'cat': cat})


def nova_categoria(request):
    form = CategoriaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'nova-categoria.html', {'form': form})
