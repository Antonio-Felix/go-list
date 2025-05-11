from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import FormCadastro, FormLogin
from django.contrib.auth.decorators import login_required

def cadastro_view(request):
    if request.method == 'POST':
        form = FormCadastro(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = FormCadastro()
    return render(request, 'usuarios/cadastro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = FormLogin(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                return redirect('painel')
    else:
        form = FormLogin()
    return render(request, 'usuarios/login.html', {'form': form})

@login_required
def painel_view(request):
    return render(request, 'usuarios/painel.html', {'usuario': request.user})

def logout_view(request):
    logout(request)
    return redirect('login')
