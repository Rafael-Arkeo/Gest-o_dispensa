from django.forms import ModelForm
from produtos.models import Categoria


class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
