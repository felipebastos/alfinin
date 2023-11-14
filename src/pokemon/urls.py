from django.urls import path, include
from rest_framework import routers

from pokemon.viewsets import AmbienteView, PokemonView, PokeAmbView

router = routers.DefaultRouter()
router.register(r"ambientes", AmbienteView)
router.register(r"pokemon", PokemonView, basename="pokemon")
router.register(r"pokeamb", PokeAmbView)


urlpatterns = [
    path("", include(router.urls)),
]
