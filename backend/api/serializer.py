from django.db.models import fields
from rest_framework import serializers
from api.models import FotoPrincipal, FotosAcoes, TimeVoluntarios, Depoimentos, NewsLetter, NossosDados, LocaisTrabalhados

class AtualizaImagemSerializer(serializers.ModelSerializer):

    class Meta:
        model = FotoPrincipal
        fields = ('foto_principal', )


class FotoPrincipalSerializer(serializers.ModelSerializer):

    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = FotoPrincipal
        fields = '__all__'

    def get_image_url(self, obj):
        return obj.foto_principal.url

class FotosAcoesSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = FotosAcoes
        fields = ('id', 'foto', 'image_url', 'frase')

    def get_image_url(self, obj):
        return obj.foto.url

class TimeVoluntariosSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = TimeVoluntarios
        fields = '__all__'

    def get_image_url(self, obj):
        return obj.foto.url

class DepoimentosSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Depoimentos
        fields = '__all__'

    def get_image_url(self, obj):
        return obj.foto.url


class NewsLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLetter
        fields = '__all__'

class LocaisTrabalhadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocaisTrabalhados
        fields = '__all__'

class NossosDadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = NossosDados
        fields = '__all__'