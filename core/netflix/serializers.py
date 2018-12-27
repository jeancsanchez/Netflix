from rest_framework import serializers

from netflix.models import Filme


class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = '__all__'
