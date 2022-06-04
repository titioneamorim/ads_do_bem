from django.shortcuts import render
from edital.service import EditalService
from perfil.service import PerfilService
from projeto.service import ProjetoService
from projeto.serializers import ProjetoSerializer
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect

_SERVICE_PROJETO =  ProjetoService()
_SERVICE_PERFIL = PerfilService()
_SERVICE_EDITAL = EditalService()

@login_required
def projetos(request):
    
    user = request.user.id
    
    projetos = _SERVICE_PROJETO.find_by_perfil(user)
    if projetos is None:
        return render(request, 'projetos.html', {'section': 'projetos'})
    return render(request, 'projetos.html', context={"projetos": projetos, 'section': 'projetos'})
    
def delete_projeto(request, id):
    _SERVICE_PROJETO.delete_projeto(id)
    return HttpResponseRedirect('/projeto')

def edit_projeto(request, id):
    pass

def download_projeto(request, id):
    pass

def create_projeto(request):
    editais = _SERVICE_EDITAL.find_all_editais()
    return render(request, 'projeto.html', context={'editais': editais})

def save_projeto(request, edital_id):
    pass