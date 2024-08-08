from .views import index, about, postar
from django.urls import path 

urlpatterns = [
     path('', index, name='index'),
     path('about/', about, name='about'),
     path('postar/', postar, name='postar')
]
