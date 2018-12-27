from django.contrib import admin
from django.contrib.admin import register
from django.utils.safestring import mark_safe

from netflix.models import *


class ElencoInline(admin.TabularInline):
    model = Filme.elenco.through
    verbose_name_plural = 'Elenco'


@register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    inlines = [ElencoInline, ]
    list_filter = ('produtora', 'lancamento', 'genero', 'idioma', 'estrelas')
    exclude = ('elenco',)
    readonly_fields = ['capa', ]

    def capa(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height="{height}" />'.format(
            url=obj.imagem.url,
            width=obj.imagem.width,
            height=obj.imagem.height
        ))


admin.site.register(Idioma)
admin.site.register(Produtora)
admin.site.register(Genero)
