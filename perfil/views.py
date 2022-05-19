from urllib import request
from perfil.models import Perfil

from perfil.serializers import PerfilSerializer
from rest_framework import viewsets

class PerfilViewSet(viewsets.ModelViewSet):
    serializer_class = PerfilSerializer
    queryset = Perfil.objects.filter(usuario_id=request.user.id)
    http_method_names = ['get', 'post', 'patch']
