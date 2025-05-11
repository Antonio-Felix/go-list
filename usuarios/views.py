from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import FormCadastro, FormLogin
from django.contrib.auth.decorators import login_required
from .models import Tarefa
from django.http import JsonResponse
from django.views import View


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
    tarefas = Tarefa.objects.all()
    return render(request, 'usuarios/painel.html', {'usuario': request.user, 'tarefas': tarefas})

@login_required
def adicionar_tarefa_view(request):
    if request.method == 'POST':
        tarefa = Tarefa()
        tarefa.titulo = request.POST.get('titulo')
        tarefa.usuario = request.user
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

def logout_view(request):
    logout(request)
    return redirect('login')

# class Login(View):
#     def get(self, request):
#         form = FormLogin()
#         return render(request, 'usuarios/login.html', {'form': form})

#     def post(self, request):
#         if request.method == 'POST':
#             form = FormLogin(request.POST)
#             if form.is_valid():
#                 user = authenticate(
#                     request,
#                     username=form.cleaned_data['username'],
#                     password=form.cleaned_data['password']
#                 )
#                 if user:
#                     login(request, user)
#                     return redirect('painel')
#         else:
#             form = FormLogin()
#         return render(request, 'usuarios/login.html', {'form': form})

# class Usuario(View):
#     @login_required
#     def get(self, request):
#         pass
#         # print(request)
#         # tarefas = Tarefa.objects.filter(usuario=request.user).order_by('-data_criacao')
#         # return render(request, 'usuarios/painel.html', {
#         #     'usuario': request.user,
#         #     'tarefas': tarefas
#         # })

#     @login_required
#     def post(self, request):
#         titulo = request.POST.get('titulo')
#         if titulo:
#             Tarefa.objects.create(titulo=titulo, usuario=request.user)
#             return JsonResponse({'status': 'success'})
#         return JsonResponse({'status': 'error'}, status=400)
    
# class Logout(View):
#     def get(self, request):
#         logout(request)
#         return redirect('login')

# class Deletar(View):
#     def post(self,request):
#         pass