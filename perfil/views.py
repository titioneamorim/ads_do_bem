from django.shortcuts import render
from perfil.serializers import PerfilSerializer
from django.contrib.auth.decorators import login_required

@login_required
def perfil(request):
    return render(request, 'perfil.html', {'section': 'perfil'})