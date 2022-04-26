from urllib import request
from django.shortcuts import render
from usuario.models import UsuarioModel
from perfil.models import Perfil

from usuario.serializers import UsuarioSerializer
from rest_framework import viewsets


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = UsuarioModel.objects.all()
    serializer_class = UsuarioSerializer
    http_method_names = ["post", "patch", "get", "delete"]

    