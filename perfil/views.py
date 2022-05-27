from django.shortcuts import render
from rest_framework.views import APIView
from perfil.serializers import PerfilSerializer
from perfil.service import PerfilService
from projeto.service import ProjetoService
from django.contrib.auth.decorators import login_required

# _SERVICE_PERFIL = PerfilService()
# _SERVICE_PROJETO = ProjetoService()

class PerfilView(APIView):
    pass
    # @login_required(login_url='/login')
    # def get(self, request, usuario=None):
    #     perfil = _SERVICE_PERFIL.find_by_user(request.user)
    #     if perfil is None:
    #         return render(request, template_name='perfil.html', context={'perfil': perfil})
    #     projetos = _SERVICE_PROJETO.find_by_user(request.user)
    #     return render(request, 'projetos.html', context={"projetos": projetos})
        
    # @login_required(login_url='/login')
    # def post(self, request):
    #     serializer = PerfilSerializer(data=request.data)
    #     if not serializer.is_valid():
    #         return render(request, 'perfil.html', context={'perfil': request.data})
    #     serializer.save()
    #     projetos = _SERVICE_PROJETO.find_by_user(request.user)
    #     return render(request, 'projetos.html', context={"projetos": projetos})