from django.contrib import admin
from .models import Produtos


@admin.register(Produtos)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "preco",
        "quantidade"
    ]

