from django.db import models
from datetime import datetime

# Create your models here.

class Categorias(models.Model):
    nombre = models.CharField(max_length=100)
    

class Post(models.Model):
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    fecha = models.DateField(default=datetime.now)
    autor = models.CharField(max_length=100)

class Comentarios(models.Model):
    name = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateField(default=datetime.now)
    email = models.EmailField()
    estado = models.BooleanField(default=True)


class Preguntas(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()



    