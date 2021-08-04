from rest_framework import authentication

from django.shortcuts import render
from rest_framework import viewsets

from api.serializer import AtualizaImagemSerializer, TimeVoluntariosSerializer, FotosAcoesSerializer, FotoPrincipalSerializer, DepoimentosSerializer, NewsLetterSerializer, LocaisTrabalhadosSerializer, NossosDadosSerializer
from api.models import FotoPrincipal, FotosAcoes, TimeVoluntarios, Depoimentos, NewsLetter, LocaisTrabalhados, NossosDados


class ImagemViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    queryset = FotoPrincipal.objects.all()
    serializer_class = AtualizaImagemSerializer


class ImagePrincipalUrl(viewsets.ReadOnlyModelViewSet):
    queryset = FotoPrincipal.objects.all().order_by('-id')[:1]
    serializer_class = FotoPrincipalSerializer


class FotosAcoesView(viewsets.ReadOnlyModelViewSet):
    queryset = FotosAcoes.objects.all()
    serializer_class = FotosAcoesSerializer

      
class TimeVoluntariosView(viewsets.ReadOnlyModelViewSet):
    queryset = TimeVoluntarios.objects.all()
    serializer_class = TimeVoluntariosSerializer

class DepoimentosView(viewsets.ReadOnlyModelViewSet):
    queryset = Depoimentos.objects.all()
    serializer_class = DepoimentosSerializer

class NewsLetterView(viewsets.ReadOnlyModelViewSet):
    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterSerializer

class LocaisTrabalhadosView(viewsets.ReadOnlyModelViewSet):
    queryset = LocaisTrabalhados.objects.all()
    serializer_class = LocaisTrabalhadosSerializer

class NossosDadosView(viewsets.ReadOnlyModelViewSet):
    queryset = NossosDados.objects.all()
    serializer_class = NossosDadosSerializer