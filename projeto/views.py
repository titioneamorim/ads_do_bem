from site import USER_BASE
from django.shortcuts import render
from perfil.service import PerfilService
from projeto.service import ProjetoService
from projeto.models import Projeto
from projeto.serializers import ProjetoSerializer
from django.contrib.auth.decorators import login_required

_SERVICE_PROJETO =  ProjetoService()
_SERVICE_PERFIL = PerfilService()

@login_required
def projetos(request):
    
    user = request.user.id
    
    projetos = _SERVICE_PROJETO.find_by_perfil(user)
    if projetos is None:
        return render(request, 'projetos.html', {'section': 'projetos'})
    return render(request, 'projetos.html', context={"projetos": projetos, 'section': 'projetos'})
    
def delete_projeto(request, id):
    # projetos = _SERVICE_PROJETO.find_by_perfil(id)
    # if projetos is None:
    #     return render(request, 'projetos.html', {'section': 'projetos'})
    # return render(request, 'projetos.html', context={"projetos": projetos, 'section': 'projetos'})
    pass

def edit_projeto(request, id):
    pass

def download_projeto(request, id):
    pass

def create_projeto(request):
    return render(request, 'projeto.html')

def save_projeto(request):
    pass