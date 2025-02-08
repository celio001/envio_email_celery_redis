from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa
from django.core.mail import send_mail
from PIL import Image, ImageDraw
from django.conf import settings
import os

# Create your views here.
def inscricao(request):
    return render(request, "inscricao.html")

def processa_inscricao(request):

    def criar_convite(nome, email):
        template = os.path.join(settings.STATIC_ROOT, 'img/convite.png')
        img = Image.open(template)
        img_escrever = ImageDraw.Draw(img)
        img_escrever.text((40, 270), nome, fill=(200,89,255))
        path_salvar = os.path.join(settings.MEDIA_ROOT, f'convites/{email}.png')
        img.save(path_salvar)
    
    criar_convite('celio', 'calio')
    return HttpResponse('teste')


    nome = request.POST.get('nome')
    email = request.POST.get('email')

    pessoa = Pessoa(nome=nome, email=email)
    pessoa.save()
    #send_mail(assunto, mensagem, email_que_esta_mandando)
    send_mail('CADASTRO CONFIRMADO ', 'Seu cadastro foi confirmado com sucesso', 'celiomvjunior@gmail.com', recipient_list=[email], fail_silently=False)

    return HttpResponse('teste')

