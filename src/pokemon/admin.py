from django.contrib import admin

from pokemon import models

# Register your models here.
# Se eu quiser incrementar o meu painel admin?

# Podemos adicionar busca, ordenação, melhorar a visualização, etc.
# Referência: https://docs.djangoproject.com/en/4.2/ref/contrib/admin/


@admin.action(description="ADD Morada Nova", permissions=["change"])
def add_morada_nova(pokemonadmin, request, queryset):
    morada = models.Ambiente.objects.get(nome="Morada Nova")
    for obj in queryset:
        obj.ambientes.add(morada)


class PokemonAdmin(admin.ModelAdmin):
    list_display = [
        "numero",
        "nome",
        "capturado",
        "tipo",
        "qtd_ambientes",
        "nomes_ambientes",
    ]
    ordering = ["numero", "nome"]
    search_fields = ["nome"]
    list_filter = ["tipo", "capturado"]
    actions = [add_morada_nova]

    @admin.display(description="Quantidade de Ambientes")
    def qtd_ambientes(self, obj):
        return len(obj.ambientes.all())

    @admin.display(description="Ambientes")
    def nomes_ambientes(self, obj):
        res = ""
        for ambi in obj.ambientes.all():
            res = res + ", " + ambi.nome
        return res


admin.site.register(models.Pokemon, PokemonAdmin)
admin.site.register(models.Ambiente)
admin.site.register(models.PokeAmb)
