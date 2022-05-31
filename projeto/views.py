from site import USER_BASE
from django.shortcuts import render
from perfil.service import PerfilService
from projeto.service import ProjetoService
from projeto.models import Projeto
from projeto.serializers import ProjetoSerializer
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest

_SERVICE_PROJETO =  ProjetoService
_SERVICE_PERFIL = PerfilService

@login_required
def projetos(request):
    
    user = request.user
    
    if user is None:
        projetos = _SERVICE_PROJETO.find_by_user(user)
    
    # if projetos is None:
    #     return render(request, 'projetos.html', {'section': 'projetos'})
    return render(request, 'projetos.html', context={"projetos": request})
    
# def post(self, request):
#     serializer = ProjetoSerializer(data=request.data)
#     serializer.data.__setattr__('perfil', _SERVICE_PERFIL.find_by_user(request.user))
#     if not serializer.is_valid():
#         return render(request, 'projeto.html', context={'projeto': request.data})
#     serializer.save()
#     projetos = _SERVICE_PROJETO.find_by_user(request.user)
#     return render(request, 'projetos.html', context={"projetos": projetos})