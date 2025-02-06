from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa
from django.core.mail import send_mail


# Create your views here.
def inscricao(request):
    return render(request, "inscricao.html")

def processa_inscricao(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')

    pessoa = Pessoa(nome=nome, email=email)
    pessoa.save()
    #send_mail(assunto, mensagem, email_que_esta_mandando)
    send_mail('CADASTRO CONFIRMADO ', 'Seu cadastro foi confirmado com sucesso', 'celiomvjunior@gmail.com', recipient_list=[email], fail_silently=False)

    return HttpResponse('teste')

