from django.db import models

class Author (models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Autor")
    
    class Meta:
        db_table = "authors"
