from django.shortcuts import HttpResponse, render
from django.views import View
from django.http import JsonResponse

from http import HTTPStatus

from json import loads

class Aluno:
    nome = "Manel Carlos"
    presta = "não"

    def __str__(self):
        return "Presta não"

    def __dict__(self):
        return loads('{"nome": "Jota", "presta": "não"}')



# Create your views here.
def alo(request):
    """Esta função faz o básico."""
    dicionario = {
        "nome": "Tiquinho",
        "raça": "Pinscher",
        "idade": 17,
        "duvida": [
            {
                "pergunta": "Funciona?",
                "resposta": "sim."
            },
            {
                "pergunta": "Presta?",
                "resposta": "Presta não"
            }
        ]
    }

    dicionario["idade"] = 5

    n = Aluno()

    return JsonResponse(dict(n), status=HTTPStatus.METHOD_NOT_ALLOWED)


class PrestaNao(View):
    frase = "Presta não"

    def get(self, request, *args, **kwargs):
        return render(request, "exemplo/index.html")

    def post(self, request, *args, **kwargs):
        res = HttpResponse(f"Claro que {self.frase}")
        res["nome"] = "Tiquinho"

        return res


def soma(request, a: int, b: int) -> HttpResponse:
    return HttpResponse(f"{a}+{b}={float(a)+float(b)}")


def espia(request):
    return HttpResponse(f"oi {request.GET.get('pinscher')}")
