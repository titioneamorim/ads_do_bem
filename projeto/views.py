from urllib import request
from perfil.service import PerfilService
from projeto.models import Projeto
from projeto.serializers import ProjetoSerializer
from rest_framework import viewsets

class ProjetoViewSet(viewsets.ModelViewSet):
    
    _SERVICE_Perfil = PerfilService()
    perfil = _SERVICE_Perfil.find_by_user(request.user)
    
    serializer_class = ProjetoSerializer
    queryset = Projeto.objects.filter(PERFIL = perfil.id)
    http_method_names = ['get', 'post', 'patch']