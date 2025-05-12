from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import FormCadastro, FormLogin
from django.contrib.auth.decorators import login_required
from .models import Tarefa

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
    tarefas = Tarefa.objects.filter(usuario=request.user).order_by('ordem')
    return render(request, 'usuarios/painel.html', {'usuario': request.user, 'tarefas': tarefas})

@login_required
def adicionar_tarefa_view(request):
    if request.method == 'POST':
        ultimo = Tarefa.objects.filter(usuario=request.user).order_by('-ordem').first()
        nova_ordem = ultimo.ordem + 1 if ultimo else 1

        tarefa = Tarefa(
            titulo=request.POST.get('titulo'),
            usuario=request.user,
            ordem=nova_ordem
        )
        tarefa.save()
        return redirect('painel')

@login_required
def apagarTarefaView(request, id):
    tarefa = Tarefa.objects.get(id=id)
    tarefa.delete()
    return redirect('painel')

@login_required
def apagarTodasView(request):
    user = request.user
    Tarefa.delete(usuario=user)

@login_required
def apagarTodasAllView(request, id=None):
    Tarefa.objects.filter(usuario=request.user).delete()
    return redirect('painel')

@login_required
def mover_para_cima_view(request, id):
    tarefa = Tarefa.objects.get(id=id, usuario=request.user)
    anterior = Tarefa.objects.filter(usuario=request.user, ordem__lt=tarefa.ordem).order_by('-ordem').first()
    if anterior:
        tarefa.ordem, anterior.ordem = anterior.ordem, tarefa.ordem
        tarefa.save()
        anterior.save()
    return redirect('painel')

@login_required
def mover_para_baixo_view(request, id):
    tarefa = Tarefa.objects.get(id=id, usuario=request.user)
    proxima = Tarefa.objects.filter(usuario=request.user, ordem__gt=tarefa.ordem).order_by('ordem').first()
    if proxima:
        tarefa.ordem, proxima.ordem = proxima.ordem, tarefa.ordem
        tarefa.save()
        proxima.save()
    return redirect('painel')

def logout_view(request):
    logout(request)
    return redirect('login')