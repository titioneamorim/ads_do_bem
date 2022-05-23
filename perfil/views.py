from django.shortcuts import render
from rest_framework.views import APIView
from perfil.models import Perfil
from perfil.serializers import PerfilSerializer
from perfil.service import PerfilService
from projeto.service import ProjetoService

_SERVICE_PERFIL = PerfilService()
_SERVICE_PROJETO = ProjetoService()

class PerfilView(APIView):
    
    
    def get(self, request, usuario=None):
        perfil = _SERVICE_PERFIL.find_by_user(request.user)
        if perfil is None:
            return render(request, template_name='perfil.html', context={'perfil': perfil})
        projetos = _SERVICE_PROJETO.find_by_user(request.user)
        return render(request, 'projetos.html', context={"projetos": projetos})
        
    def post(self, request):
        serializer = PerfilSerializer(data=request.data)
        if not serializer.is_valid():
            return render(request, 'perfil.html', context={'perfil': request.data})
        serializer.save()
        projetos = _SERVICE_PROJETO.find_by_user(request.user)
        return render(request, 'projetos.html', context={"projetos": projetos})