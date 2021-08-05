from django.shortcuts import render
import requests
from api.models import NewsLetter
from django.contrib.sites.shortcuts import get_current_site

def index(request):
    path = 'http://' + str(get_current_site(request))

    imagem_principal = requests.get( path + '/api/foto-principal/').json()[0]
    acoes = requests.get( path + '/api/acoes/').json()
    dados_ong = requests.get( path + '/api/nossos-dados/').json()[-1]
    voluntarios = requests.get( path + '/api/voluntarios/').json()
    depoimentos = requests.get( path + '/api/depoimentos/').json()
    locais_atendidos = requests.get( path + '/api/locais-trabalhados/').json()

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


