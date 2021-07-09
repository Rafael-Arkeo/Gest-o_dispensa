from django.db import models
from autoslug import AutoSlugField


class Categoria(models.Model):
    nome = models.CharField(max_length=250, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="nome")

    class Meta:
        ordering = ("nome",)
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome


class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name="Produto", on_delete=models.CASCADE)
    nome = models.CharField(max_length=250, null=False, blank=False, unique=True,)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="nome")
    qtd = models.PositiveIntegerField()
    disponivel = models.BooleanField(default=True)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("nome",)
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.nome
