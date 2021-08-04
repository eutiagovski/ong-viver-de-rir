from django.db import models
from django.db.models.base import Model

# Create your models here.

class FotoPrincipal(models.Model):
    foto_principal = models.ImageField(upload_to='fotoPrincipal')
    id = models.AutoField(primary_key=True, auto_created=True)

    def __str__(self):
        return str(self.id)

class FotosAcoes(models.Model):
    foto = models.ImageField(upload_to='fotosAcoes')
    frase = models.TextField(max_length=500)
    id = models.AutoField(primary_key=True, auto_created=True)
    
    def __str__(self):
        return str(self.frase)
    

class TimeVoluntarios(models.Model):
    nome = models.CharField(max_length=200)
    frase = models.TextField(max_length=500)
    foto = models.ImageField(upload_to='voluntarios')
    id = models.AutoField(primary_key=True, auto_created=True)

    def __str__(self):
        return str(self.nome)

class Depoimentos(models.Model):
    nome = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='fotoDepoimentos', null=True, blank=True)
    depoimento = models.TextField(max_length=None)
    data_add = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True, auto_created=True)
    
    def __str__(self):
        return str(self.nome)

class NewsLetter(models.Model):
    ## cadastro de e-mail para exportar lista com dados e envio de email para ONG
    email = models.TextField(max_length=100)
    nome = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True, auto_created=True)

    def __str__(self):
        return str(self.nome)

class LocaisTrabalhados(models.Model):
    local = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    categoria_escolha = [
        ('hospitais', 'Hospital'), ('viadutos', 'Viaduto'), ('casa_repousos', 'Casa De Repouso')
    ]

    categoria = models.CharField(max_length=200, choices=categoria_escolha, default='hospitais')

    def __str__(self):
        return str(self.local)

class NossosDados(models.Model):
    voluntarios = models.IntegerField()
    visitas_mes = models.IntegerField()
    pessoas_impactadas = models.IntegerField()
    horas_doadas = models.IntegerField()

    def __str__(self):
        return str(self.voluntarios)