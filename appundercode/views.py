from django.shortcuts import render
from appundercode.models import Preguntas
from django.http import HttpResponse

def Cuestionario(request):
 if request.method == "POST": 
    nombres = request.POST["nombre"]
    mails = request.POST["mail"]
    buscar = Preguntas(nombre=nombres, email=mails)
    buscar.save()
 return render(request, 'appundercode/cuestionario.html')


def Inicio(request):
 return render(request,'appundercode/index.html')


def Blog(request):
    return render(request,'appundercode/blogs.html')

def buscar_blog(request):
    return render(request, 'appundercode/blogs.html')

def resultados(request):
    nombre = request.GET['nombre']
    name = Preguntas.object.filter(nombre_icontains=nombre)
    return render(request, 'appundercoder/blogs.html', {"name": name})

