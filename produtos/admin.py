from django.contrib import admin
from .models import Categoria,Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("categoria", "nome", "slug","qtd","criado","atualizado")
