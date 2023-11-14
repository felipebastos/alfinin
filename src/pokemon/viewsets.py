from rest_framework import viewsets
from pokemon.models import Pokemon, Ambiente, PokeAmb
from pokemon.serializers import PokemonSerializer, AmbienteSerializer, PokeAmbSerializer


class PokemonView(viewsets.ModelViewSet):
    serializer_class = PokemonSerializer

    def get_queryset(self):
        """Exemplo de queryset com comportamento duplo.

        Caso o usuário esteja logado, ele receberá a resposta de uma forma, caso não, receberá de outra.

        É interessante notar que o objeto da ViewSet possui dentre seus atributos as informações
        da requisição recebida.
        """
        if self.request.user.is_authenticated:
            return Pokemon.objects.all().order_by("-nome")
        return Pokemon.objects.all().order_by("nome")


class AmbienteView(viewsets.ModelViewSet):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer


class PokeAmbView(viewsets.ModelViewSet):
    queryset = PokeAmb.objects.all()
    serializer_class = PokeAmbSerializer
