# Generated by Django 4.2.6 on 2023-10-27 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("pokemon", "0003_ambiente_pokemon_habitat"),
    ]

    operations = [
        migrations.CreateModel(
            name="PokeAmb",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("migrou", models.DateField(auto_now=True)),
                (
                    "ambiente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pokemon.ambiente",
                    ),
                ),
                (
                    "pokemon",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pokemon.pokemon",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="pokemon",
            name="ambientes",
            field=models.ManyToManyField(
                related_name="pokemons",
                through="pokemon.PokeAmb",
                to="pokemon.ambiente",
            ),
        ),
    ]
