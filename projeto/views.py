from django.shortcuts import render
from perfil.service import PerfilService
from projeto.service import ProjetoService
from projeto.models import Projeto
from projeto.serializers import ProjetoSerializer
from rest_framework.views import APIView

_SERVICE_PROJETO =  ProjetoService
_SERVICE_PERFIL = PerfilService

class ProjetoView(APIView):
    
    def get(self, request):
        projetos = _SERVICE_PROJETO.find_by_user(request.user)
        return render(request, 'projetos.html', context={"projetos": projetos})
    
    def post(self, request):
        serializer = ProjetoSerializer(data=request.data)
        serializer.data.__setattr__('perfil', _SERVICE_PERFIL.find_by_user(request.user))
        if not serializer.is_valid():
            return render(request, 'projeto.html', context={'projeto': request.data})
        serializer.save()
        projetos = _SERVICE_PROJETO.find_by_user(request.user)
        return render(request, 'projetos.html', context={"projetos": projetos})