from django.db import models
from autoslug import AutoSlugField


class Produtos(models.Model):
    name = models.CharField(max_length=100)
    descrição = models.TextField(max_length=250)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    date_post = models.DateTimeField(auto_now_add=True)
    ult_atua = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")
    quantidade = models.IntegerField()
    estoque = models.BooleanField(default=True)
    image = models.ImageField(upload_to="produtos/image", blank=True, null=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"


    def __str__(self):
        return self.name

