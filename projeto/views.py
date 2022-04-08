from urllib import request
from django.shortcuts import render
from projeto.models import Projeto
from perfil.models import Perfil
from projeto.serializers import ProjetoSerializer
from rest_framework import viewsets

class ProjetoViewSet(viewsets.ModelViewSet):
    serializer_class = ProjetoSerializer
    queryset = Projeto.objects.all()
    http_method_names = ['get', 'post', 'patch']