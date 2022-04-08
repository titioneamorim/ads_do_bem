from urllib import request
from django.shortcuts import render
from perfil.models import Perfil

from perfil.serializers import PerfilSerializer
from rest_framework import viewsets

class PerfiliIewSet(viewsets.ModelViewSet):
    serializer_class = PerfilSerializer
    queryset = Perfil.objects.all()
    http_method_names = ['get', 'post', 'patch']

