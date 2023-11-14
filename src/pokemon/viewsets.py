from rest_framework import viewsets
from pokemon.models import Pokemon, Ambiente
from pokemon.serializers import PokemonSerializer, AmbienteSerializer


class PokemonView(viewsets.ModelViewSet):
    serializer_class = PokemonSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Pokemon.objects.all().order_by("-nome")
        return Pokemon.objects.all().order_by("nome")


class AmbienteView(viewsets.ModelViewSet):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer
