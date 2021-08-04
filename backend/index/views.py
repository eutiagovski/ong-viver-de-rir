from django.shortcuts import render
from api.models import FotoPrincipal
from api.serializer import FotoPrincipalSerializer
import requests
from api.models import NewsLetter
# Create your views here.

def index(request):
    imagem_principal = requests.get('http://viverderir.tiagomachado.dev.br/api/foto-principal/').json()[0]
    acoes = requests.get('http://viverderir.tiagomachado.dev.br/api/acoes/').json()
    dados_ong = requests.get('http://viverderir.tiagomachado.dev.br/api/nossos-dados/').json()[-1]
    voluntarios = requests.get('http://viverderir.tiagomachado.dev.br/api/voluntarios/').json()
    depoimentos = requests.get('http://viverderir.tiagomachado.dev.br/api/depoimentos/').json()
    locais_atendidos = requests.get('http://viverderir.tiagomachado.dev.br//api/locais-trabalhados/').json()

    hospitais =[]
    viadutos= [] 
    casas_repouso =[]

    for i in locais_atendidos:
        if i['categoria'] == 'hospitais':
            hospitais.append(i)
        if i['categoria'] == 'viadutos':
            viadutos.append(i)
        if i['categoria'] == 'casa_repusos':
            casas_repouso.append(i)
            
    

    if request.method == "POST":
        email = request.POST["e-mail"]
        nome = request.POST["nome"]

        novo_assinante = NewsLetter()
        novo_assinante.email = email
        novo_assinante.nome = nome

        novo_assinante.save()
        print(nome, email)

    context = {
        'image_url': imagem_principal,
        'acoes': acoes,
        'dados_ong': dados_ong,
        'voluntarios': voluntarios,
        'depoimentos': depoimentos,
        'hospitais': hospitais,
        'viadutos': viadutos,
        'casas_repouso': casas_repouso,
    }
    
    return render(request, 'base.html', context)


