from django.http import HttpResponse
from django.shortcuts import render
from edital.service import EditalService
from perfil.service import PerfilService
from projeto.service import ProjetoService
from projeto.serializers import ProjetoSerializer
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.contrib import messages


# from weasyprint import HTML

_SERVICE_PROJETO =  ProjetoService()
_SERVICE_PERFIL = PerfilService()
_SERVICE_EDITAL = EditalService()

@login_required
def projetos(request):
    
    perfil = _SERVICE_PERFIL.find_by_user(request.user)
    if perfil is None:
        messages.warning(request, "Você precisa cadastrar o perfil antes de começar um projeto!")
        return HttpResponseRedirect('/perfil')
    
    projetos = _SERVICE_PROJETO.find_by_user(request.user)
    if projetos is None:
        return render(request, 'projetos.html', {'section': 'projetos'})
    return render(request, 'projetos.html', context={"projetos": projetos, 'section': 'projetos'})
    
def delete_projeto(request, id):
    _SERVICE_PROJETO.delete_projeto(id)
    messages.success(request, "Projeto excluido com sucesso!")
    return HttpResponseRedirect('/projeto')

def edit_projeto(request, id):
    editais = _SERVICE_EDITAL.find_all_editais()
    projeto = _SERVICE_PROJETO.find_by_id(id)
    projeto.inicio_execucao = str(projeto.inicio_execucao)
    projeto.fim_execucao = str(projeto.fim_execucao)
    
    return render(request, 'projeto.html', context={"projeto": projeto, "editais": editais})

def download_projeto(request, id):
    projeto = _SERVICE_PROJETO.find_by_id(id)
    perfil = _SERVICE_PERFIL.find_by_user(request.user)
    edital = _SERVICE_EDITAL.find_by_id(projeto.template.id)
    projeto.valor_total = f"R${projeto.valor_total}"
    perfil.telefone = mascara_telefone_fax(perfil.telefone)
    projeto.telefone_responsavel = mascara_telefone_fax(projeto.telefone_responsavel)
    perfil.fax = mascara_telefone_fax(perfil.fax)
    
    return render(request, f'{edital.edital}.html', context={"projeto": projeto, "perfil": perfil})

    # html_string = render_to_string(f'{edital.edital}.html', {"projeto": projeto, "perfil": perfil})
    # html = HTML(string=html_string)
    # html.write_pdf(target=f'/tmp/{edital.edital}.pdf')
    
    # fs = FileSystemStorage('/tmp')
    
    # with fs.open(f'{edital.edital}.pdf') as pdf:
    #     response = HttpResponse(pdf, content_type='application/pdf')
    #     response['Content-Disposition'] = f'attachment; filename="{edital.edital}.pdf"'
    #     return response
    
    
def create_projeto(request):
    editais = _SERVICE_EDITAL.find_all_editais()
    return render(request, 'projeto.html', context={'editais': editais})

def save_projeto(request):
    if request.POST.get('id') == '':
        serializer = ProjetoSerializer(data=request.POST)
        if not serializer.is_valid():
            messages.error(request, serializer.errors)
            return render(request, 'projeto.html')
        else:
            serializer.save()
            messages.success(request, "Projeto salvo com sucesso!")
        return HttpResponseRedirect('/projeto')
    else:
        _SERVICE_PROJETO.update_projeto(request)
        messages.success(request, "Projeto editado com sucesso!")
        return HttpResponseRedirect('/projeto')

def mascara_telefone_fax(numero):
    
    if len(numero) < 11:
        celular = str(numero)
        telFormatado = '({}) {}-{}'.format(celular[0:2]
                            ,celular[2:6], celular[6:])
        return telFormatado
    else:
        celular = str(numero)
        telFormatado = '({}) {}-{}-{}'.format(celular[0:2],
                            celular[2] ,celular[3:7], celular[7:])
        return telFormatado
    