from django.shortcuts import render, redirect, get_object_or_404
from produtos.models import Categoria
from .forms import CategoriaForm


def list_categoria(request):
    """Retorna lista de categorias"""
    cat = Categoria.objects.all()
    return render(request, 'lista-categoria.html', {'cat': cat})


def nova_categoria(request):
    form = CategoriaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list-categoria')
    return render(request, 'nova-categoria.html', {'form': form})


def nova_categoria_alternativa(request):
    """Caso o usuário crie uma nova categoria
        no formulário do "novo produto",ele será
            redirecionado para pagina de "nova categoria"
                então voltará para a pagina anterior"""
    form = CategoriaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('novo_prod')
    return render(request, 'nova-categoria.html', {'form': form})


def atualizar_categoria(request, id):
    cat = get_object_or_404(Categoria, pk=id)
    form = CategoriaForm(request.POST or None, instance=cat)

    if form.is_valid():
        form.save()
        return redirect('list-categoria')
    return render(request, 'atualizar-categoria.html', {'form': form, 'cat': cat})


def deletar_categoria(request, id):
    cat = get_object_or_404(Categoria, pk=id)
    form = CategoriaForm(request.POST or None, instance=cat)

    if request.method == 'POST':
        cat.delete()
        return redirect('list-categoria')

    return render(request, 'deletar-categoria.html', {'cat': cat})