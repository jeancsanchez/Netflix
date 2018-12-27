from rest_framework import routers

from netflix.views import FilmesViewSet

router = routers.DefaultRouter()
router.register('filmes', FilmesViewSet)
