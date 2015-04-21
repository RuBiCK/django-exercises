from django.db import models
from tweets.models import Tag

# Create your models here.

class Tipo(models.Model):
    titulo = models.CharField(max_length=50,null=False, blank=False, unique=True)

class Escritor(models.Model):
    nombre = models.CharField(max_length=100,null=False)
    apellidos = models.CharField(max_length=100,null=False)
    def nombre_completo(self):
        return self.nombre + ' ' + self.apellidos

class Noticia(models.Model):
    titulo = models.CharField(max_length=200,null=False,blank=False,default='Titulo Noticia')
    texto = models.CharField(max_length=1000,null=False, blank=False)
    pubdate = models.DateField()
    tipo = models.ForeignKey(Tipo)
    autor = models.ForeignKey(Escritor)
    tags = models.ManyToManyField(Tag) #Ampliacion 1

class Comentario(models.Model):
    texto = models.CharField(max_length=200)
    pubdate = models.DateField

