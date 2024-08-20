from .views import index, about, login, signup, logout, indexbase
from django.urls import path 

urlpatterns = [
     path('', index, name='index'),
     path('about/', about, name='about'),
    path('login/',login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
    path('indexbase/', indexbase, name='indexbase')
]
