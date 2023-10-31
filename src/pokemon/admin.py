from django.contrib import admin

from pokemon import models

# Register your models here.
admin.site.register(models.Pokemon)
admin.site.register(models.Ambiente)
admin.site.register(models.PokeAmb)
