# Create your models here.
from django.db import models


class Genero(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Gêneros'


class Ator(models.Model):
    sexos = (
        (1, 'M'),
        (2, 'F')
    )

    nome = models.CharField(max_length=100)
    sexo = models.IntegerField(choices=sexos)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Atores'


class Idioma(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=100)

    def __str__(self):
        return self.sigla

    class Meta:
        verbose_name_plural = 'Idiomas'


class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    resumo = models.TextField(max_length=100)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT)
    duracao = models.DurationField(default=0)
    elenco = models.ManyToManyField(Ator)
    link = models.URLField()
    estrelas = models.IntegerField(default=0)
    idioma = models.ForeignKey(Idioma, on_delete=models.PROTECT)
    lancamento = models.DateField()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = 'Filmes'
