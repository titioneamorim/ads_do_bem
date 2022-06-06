from django.shortcuts import render
from edital.service import EditalService
from perfil.service import PerfilService
from perfil.views import perfil
from projeto import serializers
import projeto
from projeto.service import ProjetoService
from projeto.serializers import ProjetoSerializer
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.contrib import messages

_SERVICE_PROJETO =  ProjetoService()
_SERVICE_PERFIL = PerfilService()
_SERVICE_EDITAL = EditalService()

@login_required
def projetos(request):
    
    user = request.user
    perfil = _SERVICE_PERFIL.find_by_user(user)
    if perfil is None:
        messages.warning(request, "Você precisa cadastrar o perfil antes de começar um projeto!")
        render(request, 'perfil.html')
    
    projetos = _SERVICE_PROJETO.find_by_user(user)
    if projetos is None:
        return render(request, 'projetos.html', {'section': 'projetos'})
    return render(request, 'projetos.html', context={"projetos": projetos, 'section': 'projetos'})
    
def delete_projeto(request, id):
    _SERVICE_PROJETO.delete_projeto(id)
    messages.success(request, "Projeto excluido com sucesso!")
    return HttpResponseRedirect('/projeto')

def edit_projeto(request, id):
    projeto = _SERVICE_PROJETO.find_by_id(id)
    return render(request, 'projeto.html', context={"projeto": projeto})

def download_projeto(request, id):
    projeto = _SERVICE_PROJETO.find_by_id(id)
    perfil = _SERVICE_PERFIL.find_by_user(request.user)
    return render(request, 'download.html', context={"projeto": projeto, "perfil": perfil})

def create_projeto(request):
    perfil = _SERVICE_PERFIL.find_by_user(request.user)
    if perfil is None:
        return HttpResponseRedirect('/perfil')
    editais = _SERVICE_EDITAL.find_all_editais()
    return render(request, 'projeto.html', context={'editais': editais})

def save_projeto(request):
    serializer = ProjetoSerializer(data=request.POST)
    if not serializer.is_valid():
        messages.error(request, serializer.errors)
    else:
        _SERVICE_PROJETO.save_projeto(request.POST)
    return HttpResponseRedirect('/projeto')