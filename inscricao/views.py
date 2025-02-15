from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa
from .tasks import criar_convite

# Create your views here.
def inscricao(request):
    return render(request, "inscricao.html")

def processa_inscricao(request):

    nome = request.POST.get('nome')
    email = request.POST.get('email')
    
    pessoa = Pessoa(nome=nome, email=email)
    pessoa.save()
    criar_convite.delay(nome, email)
    return render(request, 'cadastro_confirmado.html')

