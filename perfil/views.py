from django.shortcuts import render
from perfil.serializers import PerfilSerializer
from django.contrib.auth.decorators import login_required

from perfil.service import PerfilService

_PERFIL_SERVICE = PerfilService()

@login_required
def perfil(request):
    perfil = _PERFIL_SERVICE.find_by_user(request.user.id)
    if perfil is None:
        return render(request, 'perfil.html', {'section': 'perfil'})
    else:
        if request.method == 'POST':
            serializers = PerfilSerializer(data=request.data)
            
            if serializers.is_valid:
                serializers.save(usuario_id=request.user.id)
                render(request, 'projetos.html', {'section': 'projetos'})
            else:
                render(request, 'perfil.html', context={"perfil": {request.POST.get("perfil")}})
    return render(request, 'perfil.html', context={"perfil": perfil, 'section': 'perfil'})