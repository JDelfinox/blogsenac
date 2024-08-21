from .views import criar_postagem, index, about, login, signup, logout, indexbase, criar_postagem  # noqa: F811
from django.urls import path 

urlpatterns = [
     path('', index, name='index'),
     path('about/', about, name='about'),
    path('login/',login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
    path('indexbase/', indexbase, name='indexbase'),
    path('criar_postagem/', criar_postagem, name='criar_postagem')
    
]
