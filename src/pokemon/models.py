from django.db import models


# Create your models here.
POKE_TIPOS = (
    ("norm", "normal"),
    ("agua", "água"),
    ("fogo", "fogo"),
    ("gram", "grama"),
)


class Pokemon(models.Model):
    numero = models.IntegerField()
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=4, choices=POKE_TIPOS, default="norm")

    ambientes = models.ManyToManyField(
        "Ambiente", through="PokeAmb", related_name="pokemons"
    )


class Ambiente(models.Model):
    nome = models.CharField(max_length=20)


class PokeAmb(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)

    migrou = models.DateField(auto_now=True)
