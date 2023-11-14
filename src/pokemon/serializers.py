from rest_framework import serializers
from pokemon.models import Pokemon, Ambiente


class PokemonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pokemon
        fields = ["numero", "nome", "tipo", "ambientes"]


class AmbienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ambiente
        fields = ["nome"]
