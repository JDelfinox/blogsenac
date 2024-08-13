from .views import index, about, entrar, cadastro
from django.urls import path 

urlpatterns = [
     path('', index, name='index'),
     path('about/', about, name='about'),
     path('entrar/', entrar, name='entrar'),
     path('cadastro/', cadastro, name='cadastro')
     
]
