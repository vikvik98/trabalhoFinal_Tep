from rest_framework import serializers
from rest_framework_jwt.serializers import User

from filmes.models import *


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Categoria
        fields = ('id', 'nome')


class FilmeSerializer(serializers.HyperlinkedModelSerializer):
    usuario = serializers.ReadOnlyField(source='usuario.username')
    categoria = serializers.SlugRelatedField(queryset=Categoria.objects.all(), slug_field='nome')
    id = serializers.ReadOnlyField()

    class Meta:
        model = Filme
        fields = ('id', 'usuario', 'nome', 'categoria')

class UserFilmeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Filme
        fields = ('url', 'name')

class UserSerializer(serializers.HyperlinkedModelSerializer):

    filmes = UserFilmeSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'filmes')


