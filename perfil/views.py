from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from perfil.service import PerfilService
from perfil.serializers import PerfilSerializer

_PERFIL_SERVICE = PerfilService()

@login_required
def perfil(request):
    if request.method == 'GET':
        perfil = _PERFIL_SERVICE.find_by_user(request.user)
        if perfil is None:
            return render(request, 'perfil.html', {'section': 'perfil'})
        else:
            return render(request, 'perfil.html', context={"perfil": perfil, 'section': 'perfil'})
            
    if request.method == 'POST':
        perfil = _PERFIL_SERVICE.find_by_user(request.user.id)
        serializer = PerfilSerializer(instance=perfil , data=request.POST)
        
        if not serializer.is_valid():
            messages.error(request, serializer.errors.get("email_instituicao"))
            return render(request, 'perfil.html', context={"perfil": perfil, 'section': 'perfil'})
        else:
            serializer.save()
            messages.success(request, "Perfil salvo com sucesso!")
        return render(request, 'perfil.html', context={"perfil": perfil, 'section': 'perfil'})
    
def replace_mascara(numero):
    for n in "()-' '":
        numero = numero.replace(n, '')
    return numero