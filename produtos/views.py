from django.shortcuts import render
from.models import Produtos

def home(request):
    return render(request, 'home.html')


def prod_view(request):
    prod = Produtos.objects.all()
    return render(request, 'produto-list.html', {'prod': prod})
