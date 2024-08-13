from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def entrar(request):
    return render(request, 'entrar.html')

def cadastro(request):
    return render(request, 'cadastro.html')

