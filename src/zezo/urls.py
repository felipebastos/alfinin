"""
URL configuration for zezo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.shortcuts import HttpResponse, render
from django.views import View


def alo(request):
    """Esta função faz o básico."""
    return HttpResponse("Alô mamãe!")


class PrestaNao(View):
    frase = "Presta não"

    def get(self, request, *args, **kwargs):
        return render(request, "zezo/page.html")

    def post(self, request, *args, **kwargs):
        return HttpResponse(f"Claro que {self.frase}")


def soma(request, a: int, b: int) -> HttpResponse:
    return HttpResponse(f"{a}+{b}={float(a)+float(b)}")


def espia(request):
    return HttpResponse(f"oi {request.GET.get('pinscher')}")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("alo/", alo),
    path("presta/", PrestaNao.as_view()),
    path("soma/<path:a>/mais/<b>/", soma),
    path("espia/", espia),
]
