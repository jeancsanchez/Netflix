from django.contrib import admin
from django.contrib.admin import register

from netflix.models import *


@register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'resumo', 'idioma')
    list_filter = ('lancamento', 'genero', 'idioma', 'estrelas')


admin.site.register(Idioma)
admin.site.register(Ator)
admin.site.register(Produtora)
admin.site.register(Genero)
