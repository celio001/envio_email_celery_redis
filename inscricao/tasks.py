from celery import shared_task
import os
from PIL import Image, ImageDraw
from django.conf import settings
from hashlib import sha256
from django.core.mail import send_mail

@shared_task
def criar_convite(nome, email):
    template = os.path.join(settings.STATIC_ROOT, 'img/convite.png')
    img = Image.open(template)
    img_escrever = ImageDraw.Draw(img)
    img_escrever.text((40, 270), nome, fill=(200,89,255))
    chave_secreta = "SHAHSJAJSJS@#@#2314314231FGSFGSGSG"
    token = sha256((email + chave_secreta).encode()).hexdigest()
    path_salvar = os.path.join(settings.MEDIA_ROOT, f'convites/{token}.png')
    img.save(path_salvar)
    #send_mail(assunto, mensagem, email_que_esta_mandando)
    send_mail('CADASTRO CONFIRMADO ', f'Seu cadastro foi confirmado com sucesso \n Aqui está o link do seu convite: http://127.0.0.1:8000/media/convites/{token}.png', 'celiomvjunior@gmail.com', recipient_list=[email], fail_silently=False)
    return None