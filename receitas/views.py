from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
a = "SENAI"

def home(request):
    return render(request, "home.html",
        context=
                  {
                      'nome': a,
                  })

def sobre(request):
    return HttpResponse("Sobre nós")

def receita(request):
    return HttpResponse("As receitas")

def home(request):
    return render (request, 'page/home.html', context=
                   {'nome': a,})
