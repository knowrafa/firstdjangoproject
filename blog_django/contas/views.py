from django.shortcuts import render, HttpResponse

# Create your views here.


def paginaInicial(request):
    descricao = "UMA DESCRIÇÃO DINÂMICA"
    return render(request, "contas/home.html", {"des": descricao})
#    return HttpResponse("Bem vindo a página do app de contas")

def login(request):
    return render(request, "contas/login.html")

def checkout(request):
    return HttpResponse("Veja seu carrinho de compras")
