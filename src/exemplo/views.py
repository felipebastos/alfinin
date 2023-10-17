from django.shortcuts import HttpResponse, render
from django.views import View
from django.http import JsonResponse

from http import HTTPStatus


# Create your views here.
def alo(request):
    """Esta função faz o básico."""
    dicionario = {
        "nome": "Tiquinho",
        "raça": "Pinscher",
        "idade": 17,
    }

    dicionario["idade"] = 5

    return JsonResponse(dicionario, status=HTTPStatus.METHOD_NOT_ALLOWED)


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
