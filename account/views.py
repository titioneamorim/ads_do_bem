from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from perfil.service import PerfilService

from projeto.service import ProjetoService
from .forms import FormularioLogin, RegistroUsuario
from django.contrib.auth.decorators import login_required

_SERVICE_PROJETO =  ProjetoService()
_SERVICE_PERFIL = PerfilService()

def login_usuario(request):
    if request.method == 'POST':
        form = FormularioLogin(request.user, request.POST) #instanciando o formulário do forms.py

        if form.is_valid(): #verificando se o formulário é válido
            cd = form.cleaned_data
            user = authenticate(request, #verificando se o usuário existe no banco de dados
            username=cd['username'],
            password=cd['password'])

            if user is not None:
                if user.is_active:  #verificando se o usuário está ativo
                    login(request, user)    #realizando o login
                    return HttpResponse('Autenticação realizada com sucesso')

                else:
                    return HttpResponse('Conta desabilitada')

            else:
                return HttpResponse('Login inválido')

    else:
        form = FormularioLogin()
    return render(request, 'login.html', {'form': form})

@login_required
def home(request):
    perfil = _SERVICE_PERFIL.find_by_user(request.user)
    projetos = _SERVICE_PROJETO.find_by_user(request.user)
    return render(request,
        'home.html',
        {'perfil': perfil, 'projetos' : projetos, 'section': 'home'})

def index(request):
    return render(request,
        'index.html',
        {'section': 'index'})

def termo(request):
    return render(request,
        'termo.html',
        {'section': 'index'})

def registrar(request):
    if request.method == 'POST':
        user_form = RegistroUsuario(request.POST)
        if user_form.is_valid():
            #Cria um objeto para o novo usuário, mas não salva ainda
            new_user = user_form.save(commit=False)
            #Define a senha escolhida
            new_user.set_password(user_form.cleaned_data['password'])
            #Salva o objeto User
            new_user.save()
            return render(request, 'register_done.html', {'new_user': new_user})

    else:
        user_form = RegistroUsuario()
    return render(request, 'register.html', {'user_form': user_form})