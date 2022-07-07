from codecs import namereplace_errors
from django.urls import path

from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='cursos.inicio'),
    path('listar/meus-cursos', views.listar_cursos, name='cursos.listar.tudo')    
]