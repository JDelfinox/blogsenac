from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import SignUpForm, LoginForm
from django.contrib.auth import logout as auth_logout

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redireciona para a página de login após o cadastro bem-sucedido
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('indexbase')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('index')

def indexbase(request):
    return render(request, 'indexbase.html')

def criar_postagem(request):
    return render(request, "criar_postagem.html")

    
