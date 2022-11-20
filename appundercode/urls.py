from django.urls import path
from appundercode.views import *

urlpatterns = [
    path('blog/', Blog, name='blog_inicio'),
    path('inicio/', Inicio, name='index_inicio'),
    path('cuestionario/', Cuestionario, name='cuestionario_inicio')

]