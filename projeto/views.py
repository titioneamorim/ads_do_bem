from django.shortcuts import render
from edital.service import EditalService
from perfil.service import PerfilService
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
    
    perfil = _SERVICE_PERFIL.find_by_user(request.user)
    if perfil is None:
        messages.warning(request, "Você precisa cadastrar o perfil antes de começar um projeto!")
        return HttpResponseRedirect('/perfil')
    
    projetos = _SERVICE_PROJETO.find_by_user(request.user)
    if projetos is None:
        return render(request, 'projetos.html', {'section': 'projetos'})
    return render(request, 'projetos.html', context={"projetos": projetos, 'section': 'projetos'})
    
def delete_projeto(request, id):
    _SERVICE_PROJETO.delete_projeto(id)
    messages.success(request, "Projeto excluido com sucesso!")
    return HttpResponseRedirect('/projeto')

def edit_projeto(request, id):
    editais = _SERVICE_EDITAL.find_all_editais()
    projeto = _SERVICE_PROJETO.find_by_id(id)
    projeto.inicio_execucao = str(projeto.inicio_execucao)
    projeto.fim_execucao = str(projeto.fim_execucao)
    
    return render(request, 'projeto.html', context={"projeto": projeto, "editais": editais})

def download_projeto(request, id):
    projeto = _SERVICE_PROJETO.find_by_id(id)
    perfil = _SERVICE_PERFIL.find_by_user(request.user)
    edital = _SERVICE_EDITAL.find_by_id(projeto.template.id)
    return render(request, f'{edital.edital}.html', context={"projeto": projeto, "perfil": perfil})

def create_projeto(request):
    editais = _SERVICE_EDITAL.find_all_editais()
    return render(request, 'projeto.html', context={'editais': editais})

def save_projeto(request):
    if request.POST.get('id') == '':
        serializer = ProjetoSerializer(data=request.POST)
        if not serializer.is_valid():
            messages.error(request, serializer.errors)
            return render(request, 'projeto.html')
        else:
            serializer.save()
            messages.success(request, "Projeto salvo com sucesso!")
        return HttpResponseRedirect('/projeto')
    else:
        _SERVICE_PROJETO.update_projeto(request)
        messages.success(request, "Projeto editado com sucesso!")
        return HttpResponseRedirect('/projeto')
