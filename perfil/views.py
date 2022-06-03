from operator import contains
from django.shortcuts import render
from perfil.models import Perfil
from perfil.serializers import PerfilSerializer
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.contrib import messages


from perfil.service import PerfilService

_PERFIL_SERVICE = PerfilService()

@login_required
def perfil(request):
    if request.method == 'GET':
        perfil = _PERFIL_SERVICE.find_by_user(request.user.id)
        if perfil is None:
            return render(request, 'perfil.html', {'section': 'perfil'})
        else:
            return render(request, 'perfil.html', context={"perfil": perfil, 'section': 'perfil'})
            
            
    if request.method == 'POST':
        perfil = _PERFIL_SERVICE.find_by_user(request.user.id)
        if perfil is None:
            perfil = Perfil()
        perfil.usuario = request.user
        perfil.bairro = request.POST.get('bairro')
        perfil.cidade = request.POST.get('cidade')
        perfil.dirigente = request.POST.get('dirigente')
        perfil.email_instituicao = request.POST.get('email_instituicao')
        perfil.fax = replace_mascara(request.POST.get('fax'))
        perfil.logradouro = request.POST.get('logradouro')
        perfil.nome_instituicao = request.POST.get('nome_instituicao')
        perfil.numero = request.POST.get('numero')
        perfil.telefone = replace_mascara(request.POST.get('telefone'))
        perfil.UF = request.POST.get('UF')
        perfil.site = request.POST.get('site')
        perfil.save()
        if perfil.pk is not None:
            messages.success(request, "Perfil salvo com sucesso!")
        else:
            messages.warning(request, "Erro ao cadastrar perfil, tente novamente!")
        return render(request, 'perfil.html', context={"perfil": perfil, 'section': 'perfil'})
        
def replace_mascara(numero):
    for n in "()-' '":
        numero = numero.replace(n, '')
    return numero