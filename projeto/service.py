from edital.service import EditalService
from perfil.service import PerfilService
from projeto.models import Projeto
from django.db.models.functions import Concat
from django.db.models import Q, Value


_SERVICE_PERFIL = PerfilService()
_SERVICE_EDITAL = EditalService()


class ProjetoService():
    
    def find_by_user(self, user):
        perfil = _SERVICE_PERFIL.find_by_user(user)
        if perfil is None:
            return None
        return Projeto.objects.filter(perfil_id=perfil.id).order_by('-modified')
    
    def delete_projeto(self, id):
        return Projeto.objects.filter(id=id).delete()
    
    def find_by_id(self, id) -> Projeto:
        projeto = Projeto.objects.filter(id=id)
        if len(projeto) == 0:
            return None
        return projeto[0]
    
    def find_by_nome_resumo(self, str, user):
        perfil = _SERVICE_PERFIL.find_by_user(user)
        projetos = Projeto.objects.filter(Q(nome_projeto__icontains=str) | Q(resumo_objetivos__icontains=str) | 
            Q(nome_responsavel__icontains=str) | Q(titulo__icontains=str), perfil_id=perfil.id).order_by('-modified')
        if len(projetos) == 0:
            return None
        return projetos
