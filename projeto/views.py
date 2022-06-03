from site import USER_BASE
from django.shortcuts import render
from perfil.service import PerfilService
from projeto.service import ProjetoService
from projeto.models import Projeto
from projeto.serializers import ProjetoSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

_SERVICE_PROJETO =  ProjetoService()
_SERVICE_PERFIL = PerfilService()

@login_required
def projetos(request):
    
    user = request.user.id
    
    projetos = _SERVICE_PROJETO.find_by_perfil(user)
    if projetos is None:
        return render(request, 'projetos.html', {'section': 'projetos'})
    return render(request, 'projetos.html', context={"projetos": projetos, 'section': 'projetos'})
    
def projeto(request):
    pass