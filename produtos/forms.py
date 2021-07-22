from django.forms import ModelForm
from .models import Produto


class ProdForms(ModelForm):
    """Cria um formulário com o modelo da classe
            Produto"""
    class Meta:
        model = Produto
        fields = ['categoria', 'nome',  'qtd', 'disponivel']