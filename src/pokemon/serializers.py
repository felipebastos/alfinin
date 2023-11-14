from rest_framework import serializers
from pokemon.models import Pokemon, Ambiente, PokeAmb


class PokemonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pokemon
        fields = ["url", "numero", "nome", "tipo", "ambientes"]


class AmbienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ambiente
        fields = ["url", "nome"]


class PokeAmbSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PokeAmb
        fields = ["url", "pokemon", "ambiente", "migrou"]
