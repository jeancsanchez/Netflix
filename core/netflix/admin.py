from django.contrib import admin
from django.contrib.admin import register

from netflix.models import *


class ElencoInline(admin.TabularInline):
    model = Filme.elenco.through
    verbose_name_plural = 'Elenco'


@register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    inlines = [ElencoInline, ]
    list_display = ('titulo', 'resumo', 'idioma')
    list_filter = ('lancamento', 'genero', 'idioma', 'estrelas')
    exclude = ('elenco',)


admin.site.register(Idioma)
admin.site.register(Produtora)
admin.site.register(Genero)
