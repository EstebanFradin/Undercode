from django.http import HttpResponse
from datetime import datetime
from django.template import loader
from django.template import Context,Template,render
from appundercode.models import *

def blog_categoria(request):     
    categoria = Categorias(nombre='Viajes')     
    categoria.save()     

def blog_post(request):
    post = Post(titulo='España - Islas canarias', contenido='El principal motivo por el que los turistas viajan a las Islas Canarias es sin duda por el sol y sus playas.', fecha=datetime(datetime.now), autor='Esteban')    
    post.save()  

def blog_comentarios(request):   
    comentario = Comentarios(name='Juan', contenido='Muy buen articulo, me ayudó mucho', fecha=datetime(datetime.now), email='juantutor@hotmail.com', estado='True')     
    comentario.save()     
    return render(request, '')  
    
# def blog_base(request):      
#     familiar = familiar1.objects.all()      
#     contexto = {'blog_base':familiar}      
#     return render(request, '', contexto)