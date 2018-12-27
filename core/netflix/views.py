from rest_framework import viewsets

from netflix.models import Filme
from netflix.serializers import FilmeSerializer


class FilmesViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
