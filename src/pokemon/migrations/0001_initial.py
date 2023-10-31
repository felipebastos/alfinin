# Generated by Django 4.2.6 on 2023-10-24 22:18

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pokemon",
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
                ("numero", models.IntegerField()),
                ("nome", models.CharField(max_length=200)),
                ("tipo", models.CharField(max_length=5)),
            ],
        ),
    ]