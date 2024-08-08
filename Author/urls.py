from .views import contato, post1, post2, post3, post4
from django.urls import path 

urlpatterns = [
     path('contato/', contato, name='contato'),
     path('post1/', post1, name='post1' ),
     path('post2/', post2, name='post2' ),
     path('post3/', post3, name='post3' ),
     path('post4/', post4, name='post4' ),
     
]